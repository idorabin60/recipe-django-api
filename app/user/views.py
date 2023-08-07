from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, authentication, permissions
from user.serializers import UserSerializer, AuthTokenSerialzier
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokeView(ObtainAuthToken):
    serializer_class = AuthTokenSerialzier
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            token = Token.objects.get(user=user)
            token.invalidated = True
            token.delete()
        except Token.DoesNotExist:
            pass

        request.auth = None  # Remove the authentication token from the request
        request.user = None  # Remove the user from the request

        return Response(status=status.HTTP_200_OK)


class ManagaUserView(generics.RetrieveUpdateAPIView):
    """Manage the auth user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """rertrive and return the auth user"""
        return self.request.user

    def get_serializer_context(self):
        """
        Additional context provided to the serializer.
        Include the authentication token in the context.
        """
        context = super().get_serializer_context()
        user = self.request.user
        token, created = Token.objects.get_or_create(user=user)
        context['token'] = token.key
        return context
