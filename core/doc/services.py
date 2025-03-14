from .models import Document

def save_documents(validated_data):
    title = validated_data['title']
    files = validated_data['files']
    documents = []
    for file in files:
        document = Document.objects.create(title=title, file=file)
        documents.append(document)
    return documents
