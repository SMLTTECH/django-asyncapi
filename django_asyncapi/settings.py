from django.conf import settings
from pydantic import PyObject, BaseModel


class DjangoAsyncapiSettings(BaseModel):
    ASYNCAPI_SPEC_CLASS: list[PyObject] | PyObject


DJANGO_ASYNCAPI_SETTINGS = getattr(settings, "DJANGO_ASYNCAPI", {})
django_asyncapi_settings = DjangoAsyncapiSettings(**DJANGO_ASYNCAPI_SETTINGS)
