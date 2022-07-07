from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, PostViewSet

v1_router = SimpleRouter()
v1_router.register('v1/groups', GroupViewSet)
v1_router.register('v1/posts', PostViewSet)


urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
