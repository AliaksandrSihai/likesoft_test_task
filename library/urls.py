from django.urls import path
from library.apps import LibraryConfig
from library import views
from rest_framework import routers

from library.views import BookViewSet

app_name = LibraryConfig.name


book_router = routers.DefaultRouter()
book_router.register(r'book', BookViewSet, basename='book')


urlpatterns = [
    path('authors/', views.ListAuthorAPIView.as_view(), name='authors_list'),
] + book_router.urls