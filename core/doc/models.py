from django.db import models
from core.common.models import BaseModel

class Document(BaseModel):
    """
    A model representing a document.

    Attributes
    ----------
    title : str
        The title of the document.
    file : File
        The file associated with the document.
    uploaded_at : datetime
        The date and time when the document was uploaded.
    """

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the document.

        Returns
        -------
        str
            The title of the document.
        """
        return self.title