from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import GroupView

v1_router = SimpleRouter()
v1_router.register('v1/groups', GroupView)


urlpatterns = [
    path('', include(v1_router.urls)),
]
