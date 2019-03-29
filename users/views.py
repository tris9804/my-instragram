from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (IsAdminUser, IsAuthenticatedOrReadOnly,)

from .models import User, Relationship
from .serializers import UserSerializer, RelationshipSerializer
from .permissions import IsSelf

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):

        serializer = super().get_serializer_class()
        if self.action == 'follow':
            return RelationshipSerializer
        return serializer

    def get_permissions(self):
        if self.action == 'create':
            return []

        permissions = super().get_permissions()

        if self.action == 'destroy':
            permissions.append(IsAdminUser())

        if self.action in ['update', 'partial_update']:
            permissions.append(IsSelf())

        return permissions
    @action(['POST'], True)
    def follow(self, request, pk):
        to_user = self.get_object()
        from_user = request.user

        # relationship = Relationship.objects.create(
        #     to_user=to_user,
        #     from_user=from_user,
        #     is_agreed=to_user.is_public,
        # )

        serializer = self.get_serializer(data={
            'to_user': to_user.id,
            'from_user': from_user.id,
            'is_agreed': to_user.is_public,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'ok'})

