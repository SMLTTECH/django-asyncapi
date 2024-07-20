from django.conf import settings

from django_asyncapi.settings import DjangoAsyncapiSettings

DJANGO_ASYNCAPI_SETTINGS = getattr(settings, "DJANGO_ASYNCAPI", {})
django_asyncapi_settings = DjangoAsyncapiSettings(**DJANGO_ASYNCAPI_SETTINGS)
