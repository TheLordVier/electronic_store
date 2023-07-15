from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User_Model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания нового пользователя
    """
    class Meta:
        model = User_Model
        fields = ("username", "first_name", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        instance = User_Model.objects.create_user(**validated_data)
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    """
    Сериализатор для входа пользователя
    """
    username = serializers.CharField(max_length=60)

    class Meta:
        model = User_Model
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        instance = authenticate(
            username=self.validated_data.get("username"),
            password=self.validated_data.get("password"),
        )
        if not instance or not instance.is_active:
            raise ValidationError({"Ошибка входа": "Вы ввели неправильный логин или пароль"})

        login(self.context["request"], instance)
        return instance


class UserLogoutSerializer(serializers.Serializer):
    """
    Сериализатор для выхода пользователя
    """
    pass
