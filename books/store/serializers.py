from rest_framework.serializers import ModelSerializer


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields='__all__'

