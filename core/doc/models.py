from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class UploadedFile(BaseModel):
    file = models.FileField(upload_to='uploads/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or str(self.file)