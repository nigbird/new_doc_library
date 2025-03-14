from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Document

class DocumentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.upload_url = reverse('document-upload')
        self.list_url = reverse('document-list')

    def test_upload_documents(self):
        with open('test_file1.txt', 'w') as f:
            f.write('This is a test file.')
        with open('test_file2.txt', 'w') as f:
            f.write('This is another test file.')

        with open('test_file1.txt', 'rb') as f1, open('test_file2.txt', 'rb') as f2:
            response = self.client.post(self.upload_url, {
                'title': 'Test Document',
                'files': [f1, f2]
            }, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Document.objects.count(), 2)
        self.assertEqual(Document.objects.first().title, 'Test Document')

    def test_list_documents(self):
        Document.objects.create(title='Test Document 1', file='test_file1.txt')
        Document.objects.create(title='Test Document 2', file='test_file2.txt')

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Document 1')
        self.assertEqual(response.data[1]['title'], 'Test Document 2')