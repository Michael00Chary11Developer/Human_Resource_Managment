from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination


class BaseModelViewSet(viewsets.ModelViewSet):

    """
        Base viewset to handle user_id assignment on create.
    """

    def perform_create(self, serializer):
        """
            Override to add the user_id to the instance.
        """

        if self.request.user.is_authenticated:
            serializer.save(user_id=self.request.user)
        else:
            try:
                default_user = User.objects.get(pk=1)
                serializer.save(user_id=default_user)
            except User.DoesNotExist:
                raise NotFound('Default user not found.')

    def get_queryset(self):
        query_set = super().get_queryset()
        
        limit=self.request.query_params.get('limit')
        offset=self.request.query_params.get("offset")
        
        if limit is not None and offset is not None:
            self.pagination_class=LimitOffsetPagination
            self.pagination_class.default_limit=int(limit)