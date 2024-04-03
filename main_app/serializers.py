from rest_framework import serializers
from .models import User, Paragraph, WordIndex

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'date_of_birth', 'created_at', 'updated_at']


class ParagraphSerializer(serializers.ModelSerializer):
    """
    Serializer for the Paragraph model.
    """
    class Meta:
        model = Paragraph
        fields = ['id', 'content']


class WordIndexSerializer(serializers.ModelSerializer):
    """
    Serializer for the WordIndex model.
    """
    class Meta:
        model = WordIndex
        fields = ['id', 'word', 'paragraph', 'frequency']
