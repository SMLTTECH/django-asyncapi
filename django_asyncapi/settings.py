from pydantic import PyObject, BaseModel, Field


class DjangoAsyncapiSettings(BaseModel):
    ASYNCAPI_SPEC_CLASS: list[PyObject] | PyObject = Field(
        ...,
        description="Path to class containing entrypoint for defining root of asyncapi specification"
    )
