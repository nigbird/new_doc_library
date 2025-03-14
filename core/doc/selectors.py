from .models import Document

def get_all_documents():
    return Document.objects.all()
