from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException
from .serializers import DocumentInputSerializer, DocumentOutputSerializer
from .services import save_documents
from .selectors import get_all_documents

class DocumentUploadView(APIView):
    serializer_class = DocumentInputSerializer

    def post(self, request, *args, **kwargs):
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
    serializer_class = DocumentOutputSerializer

    def get(self, request, *args, **kwargs):
        try:
            documents = get_all_documents()
            serializer = self.serializer_class(documents, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(f"Exception: {e}")
            raise APIException("An error occurred while retrieving documents.")
