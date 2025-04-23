from django.urls import path
from .views import DocumentUploadView, DocumentListView, FileShareView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('documents/upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('documents/share/', FileShareView.as_view(), name='file-share'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
