from rest_framework import viewsets
from .serializers import UserProfileSerializer, ProfileFeedItemSerializer
from .models import UserProfile, ProfileFeedItem
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile, UpdateOwnStatus
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    # Para hacer filtros
    filter_backends = (SearchFilter,)
    search_fields = ('name','email',)
    
class UserLoginAPIView (ObtainAuthToken):
    """Handle create user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (
        UpdateOwnStatus,
        # IsAuthenticatedOrReadOnly,
        IsAuthenticated
    )
    def perform_create(self, serializer):
        """Set the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)