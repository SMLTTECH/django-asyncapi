from asyncapi_container.asyncapi.generators.v3.generator import AsyncAPISpecV3Generator
from django.http import JsonResponse
from django.views.generic import TemplateView, View

from django_asyncapi.utils import retrieve_asyncapi_spec_containers, retrieve_merged_asyncapi_container


class AsyncAPIV3DocsView(TemplateView):
    template_name = "asyncapi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asyncapi_generator = AsyncAPISpecV3Generator(
            asyncapi_spec_container=retrieve_merged_asyncapi_container()
        )

        spec_containers = retrieve_asyncapi_spec_containers()
        first_spec_container = spec_containers[0]

        config = {
            "title": first_spec_container.info.title,
            "version": first_spec_container.info.version,
            "schema": asyncapi_generator.as_json(),
            "config": {
                "show": {
                    "sidebar": True,
                    "info": True,
                    "servers": True,
                    "operations": True,
                    "messages": True,
                    "schemas": True,
                    "errors": True,
                },
                "expand": {
                    "messageExamples": False,
                },
                "sidebar": {
                    "showServers": "byDefault",
                    "showOperations": "byDefault",
                },
            },
        }

        context["asyncapi_json"] = config

        context["service_title"] = first_spec_container.info.title
        return context


class AsyncAPIV3JsonView(View):
    def get(self, request, *args, **kwargs):
        asyncapi_generator = AsyncAPISpecV3Generator(
            asyncapi_spec_container=retrieve_merged_asyncapi_container()
        )
        asyncapi: dict = asyncapi_generator.as_dict()

        return JsonResponse(data=asyncapi, json_dumps_params={"ensure_ascii": False, "indent": 3})
