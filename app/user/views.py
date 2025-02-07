from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer,AuthTokenSerializer


class CreateUserView(generics.CreateAPIView): 
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    # queryset = get_user_model().objects.all()

class AuthTokenView(ObtainAuthToken):
    
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES