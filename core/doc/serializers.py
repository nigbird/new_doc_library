from rest_framework import serializers
from .models import Document

class DocumentInputSerializer(serializers.Serializer):
    """
    Serializer for inputting document data.

    Attributes
    ----------
    title : CharField
        The title of the document.
    files : ListField
        A list of files to be uploaded.
    """
    title = serializers.CharField(max_length=255)
    files = serializers.ListField(
        child=serializers.FileField(),
        allow_empty=False
    )

class DocumentOutputSerializer(serializers.ModelSerializer):
    """
    Serializer for outputting document data.

    Meta Attributes
    ---------------
    model : Document
        The model that is being serialized.
    fields : list
        The fields that are included in the serialized output.
    """
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'uploaded_at']

class FileShareInputSerializer(serializers.Serializer):
    """
    Serializer for sharing a document via email.

    Attributes
    ----------
    file_id : UUIDField
        The ID of the document to be shared.
    recipient_email : EmailField
        The email address of the recipient.
    """
    file_id = serializers.UUIDField()
    recipient_email = serializers.EmailField()


