from rest_framework import generics, status
from rest_framework.response import Response

from users.tasks import welcome_message
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Эндпоинт регистрации нового пользователя """

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user_email = response.data.get('email')
            #welcome_message.delay(user_email)
        return response

