
from users.apps import UsersConfig
from django.urls import path

from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='user')
]
