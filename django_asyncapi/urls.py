from django.urls import path

from django_bus.views.asyncapi import AsyncAPIV3DocsView, AsyncAPIV3JsonView


urlpatterns = [
    path("asyncapi/v3/", AsyncAPIV3DocsView.as_view()),
    path("asyncapi/v3/json/", AsyncAPIV3JsonView.as_view()),
]
