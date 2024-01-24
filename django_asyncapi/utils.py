from collections import defaultdict

from asyncapi_container.containers.v3.simple_spec import SimpleSpecV3

from django_asyncapi.settings import django_asyncapi_settings


class BusRoutingsMerger:
    """Merge a list of bus routing instances into one BusRouting instance."""

    def merge(self, asyncapi_specs: list[SimpleSpecV3]) -> SimpleSpecV3:
        first_spec = asyncapi_specs[0]

        merged_produces_routing_map = defaultdict(list)
        merged_consumes_routing_map = defaultdict(list)

        for asyncapi_spec in asyncapi_specs:
            for topic_name, messages in asyncapi_spec.sends.items():
                merged_produces_routing_map[topic_name].extend(messages)
                # deduplicate
                deduplicated_messages: set = set(merged_produces_routing_map[topic_name])
                deduplicated_messages: list = list(deduplicated_messages)
                merged_produces_routing_map[topic_name] = deduplicated_messages

            for topic_name, messages in asyncapi_spec.receives.items():
                merged_consumes_routing_map[topic_name].extend(messages)
                # deduplicate
                deduplicated_messages: set = set(merged_consumes_routing_map[topic_name])
                deduplicated_messages: list = list(deduplicated_messages)
                merged_consumes_routing_map[topic_name] = deduplicated_messages

        return SimpleSpecV3(
            info=first_spec.info,
            sends=merged_produces_routing_map,
            receives=merged_consumes_routing_map,
        )


def retrieve_asyncapi_spec_containers() -> list[SimpleSpecV3]:
    asyncapi_spec_classes = django_asyncapi_settings.ASYNCAPI_SPEC_CLASS
    if not isinstance(asyncapi_spec_classes, list):
        asyncapi_spec_classes = [asyncapi_spec_classes]

    asyncapi_spec_classes = [spec_class() for spec_class in asyncapi_spec_classes]

    return asyncapi_spec_classes


def retrieve_merged_asyncapi_container() -> SimpleSpecV3:
    asyncapi_spec_containers = retrieve_asyncapi_spec_containers()
    merger = BusRoutingsMerger()
    return merger.merge(asyncapi_specs=asyncapi_spec_containers)
