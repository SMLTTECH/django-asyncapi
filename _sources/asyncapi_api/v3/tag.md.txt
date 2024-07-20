# Tag


```{eval-rst}
.. automodule:: asyncapi_container.asyncapi.spec.v3.tag
    :members:


```



```python

class Customer(BaseModel):
    first_name: str = Field(..., title='First Name')
    last_name: str = Field(..., title='Last Name')
    email: str = Field(..., title='Email')
    country: str = Field(..., title='Country')
    zipcode: str = Field(..., title='Zipcode')
    city: str = Field(..., title='City')
    street: str = Field(..., title='Street')
    apartment: str = Field(..., title='Apartment')


class OrderSchemaV1(BaseModel):
    product_id: int = Field(..., title='Product Id')
    quantity: int = Field(..., title='Quantity')
    customer: Customer


class MySpecialServiceAsyncAPISpecV3(SimpleSpecV3):
    info: Info = Info(
        title="My special Service",
        version="1.0.0",
        description="Service for making orders"
    )
    sends: RoutingMap = {}
    receives: RoutingMap = {
        TopicV3(
            address="test.topic.v1",
            title="TESTING TITLE",
            description="test",
            summary="testing summary",
            tags=[
                Tag(name="test"),
            ]
        ): [
            Customer
        ]
    }
```