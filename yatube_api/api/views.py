from rest_framework import viewsets

from posts.models import Group
from .serializers import GroupSerializer


class GroupView(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []
