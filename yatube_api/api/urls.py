from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet

v1_router = SimpleRouter()
v1_router.register(r'v1/groups', GroupViewSet)
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename="comments")


urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
