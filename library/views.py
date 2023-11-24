from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from library.models import Author, Book
from library.pagination import ListPagination
from library.serializers import AuthorSerializer, BookSerializer


class ListAuthorAPIView(generics.ListAPIView):
    """ Просмотр всех авторов """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    pagination_class = ListPagination
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """ CRUD для модели Book"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = ListPagination
    permission_classes = [IsAuthenticated]