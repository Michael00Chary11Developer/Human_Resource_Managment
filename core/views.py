from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User


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
