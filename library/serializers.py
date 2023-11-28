from rest_framework import serializers

from library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Author"""

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Book """

    class Meta:
        model = Book
        fields = '__all__'
