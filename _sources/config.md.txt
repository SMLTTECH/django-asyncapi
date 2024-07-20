# Settings

1. Add `djanog-asyncapi` to `INSTALLED_APPS`
```python 
INSTALLED_APPS = [
    ...,
    "django_asyncapi",
]
```

2. Setup configuration inside `settings.py`
```python

DJANGO_ASYNCAPI = {
    "ASYNCAPI_SPEC_CLASS": "bus.routing.MySpecialServiceAsyncAPISpecV3",
}
 
```

3. Add `django-asyncapi` urls

```python
from django.urls import path, include

urlpatterns = [
    path('docs/', include('django_asyncapi.urls')),
]

```



```{eval-rst}
.. automodule:: django_asyncapi.settings
    :members:


```
