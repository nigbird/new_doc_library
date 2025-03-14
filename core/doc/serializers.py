from rest_framework import serializers
from .models import Document

class DocumentInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    files = serializers.ListField(
        child=serializers.FileField(),
        allow_empty=False
    )

class DocumentOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'uploaded_at']
