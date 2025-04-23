from .models import Document

def get_all_documents():
    """
    Retrieve all documents from the database.

    Returns
    -------
    QuerySet
        A QuerySet containing all Document instances.
    """
    return Document.objects.all()
