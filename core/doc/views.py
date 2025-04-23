from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException
from .serializers import DocumentInputSerializer, DocumentOutputSerializer
from .services import save_documents
from .selectors import get_all_documents
from .serializers import FileShareInputSerializer
from .services import send_file_email
from .models import Document
from django.shortcuts import get_object_or_404
from urllib.parse import urlencode

class DocumentUploadView(APIView):
    """
    API view for uploading multiple documents.

    Attributes
    ----------
    serializer_class : DocumentInputSerializer
        The serializer class used for validating the input data.
    """

    serializer_class = DocumentInputSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to upload multiple documents.

        Parameters
        ----------
        request : Request
            The request object containing the input data.

        Returns
        -------
        Response
            A response object containing the serialized data of the created documents
            or the validation errors.
        """
        try:
            data = {
                'title': request.data.get('title'),
                'files': request.FILES.getlist('files')
            }
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                documents = save_documents(serializer.validated_data)
                return Response(DocumentOutputSerializer(documents, many=True).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Exception: {e}")
            raise APIException("An error occurred while uploading documents.")

class DocumentListView(APIView):
    """
    API view for listing all documents.

    Attributes
    ----------
    serializer_class : DocumentOutputSerializer
        The serializer class used for serializing the output data.
    """

    serializer_class = DocumentOutputSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve all documents.

        Parameters
        ----------
        request : Request
            The request object.

        Returns
        -------
        Response
            A response object containing the serialized data of all documents.
        """
        try:
            documents = get_all_documents()
            serializer = self.serializer_class(documents, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(f"Exception: {e}")
            raise APIException("An error occurred while retrieving documents.")
        

class FileShareView(APIView):
    """
    API view for generating a mailto link to share a document via email.
    """

    def post(self, request, *args, **kwargs):
        file_id = request.data.get("file_id")
        recipient_email = request.data.get("recipient_email")

        # Validate inputs
        if not file_id or not recipient_email:
            return Response({"error": "file_id and recipient_email are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Get the document
        document = get_object_or_404(Document, id=file_id)

        # Generate the file URL
        file_url = f"{request.build_absolute_uri(document.file.url)}"

        # Generate the mailto link
        subject = "Shared Document"
        body = f"Here is the document you requested: {file_url}"
        mailto_link = f"mailto:{recipient_email}?{urlencode({'subject': subject, 'body': body})}"

        return Response({"mailto_link": mailto_link}, status=status.HTTP_200_OK)
