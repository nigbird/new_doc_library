from django.urls import include, path
from django.urls.resolvers import URLResolver

urlpatterns: list[URLResolver] = [
    path("auth/", include(("core.authentication.urls", "authentication"), namespace="authentication")),
    path("doc/", include(("core.doc.urls", "authentication"), namespace="doc")),

]
