from django.contrib.auth import get_user_model, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, GenericAPIView

from core.serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer

User_Model = get_user_model()


class ListCreateUserView(ListCreateAPIView):
    """
    Представление для создания и получения списка пользователей
    """
    model = User_Model
    queryset = model.objects.all()
    serializer_class = UserSerializer


class RetrieveDestroyUserView(RetrieveDestroyAPIView):
    """
    Представление для получения и удаления конкретного пользователя
    """
    model = User_Model
    queryset = model.objects.all()
    serializer_class = UserSerializer


class UserLogin(CreateAPIView):
    """
    Представление для входа пользователя
    """
    model = User_Model
    serializer_class = UserLoginSerializer


class UserLogout(GenericAPIView):
    """
    Представление для выхода пользователя
    """
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status.HTTP_200_OK)
