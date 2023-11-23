from django.urls import path
from library.apps import LibraryConfig
from library import views

app_name = LibraryConfig.name


urlpatterns = [
    path('authors/', views.ListAuthorAPIView.as_view(), name='authors_list'),
]