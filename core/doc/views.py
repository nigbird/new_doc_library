from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import UploadedFile
from .serializers import UploadedFileSerializer
import logging

logger = logging.getLogger(__name__)

class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')  # Retrieve the list of files
        logger.debug(f"Files received: {files}")
        results = []  # Initialize the results list
        for file in files:
            logger.debug(f"Processing file: {file.name}")
            serializer = self.get_serializer(data={'file': file, 'description': request.data.get('description', '')})
            if serializer.is_valid():
                serializer.save()
                results.append(serializer.data)
                logger.debug(f"File saved: {serializer.data}")
            else:
                logger.debug(f"Serializer errors: {serializer.errors}")
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        logger.debug(f"Results: {results}")
        return JsonResponse(results, safe=False, status=status.HTTP_201_CREATED)

class FileListView(generics.ListAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer