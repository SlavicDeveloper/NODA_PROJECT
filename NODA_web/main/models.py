from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.html import format_html

MEDIA_URL = "media/uploads"


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=False)
    notes_created = models.IntegerField("amount_of_notes_posted", default=0)


class Notes(models.Model):
    node_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doc_name = models.CharField(blank=False)
    doc_file = models.FileField("docx_format_field",
                                validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'])],
                                upload_to="uploads", max_length=200)

    def __str__(self):
        return self.doc_name

    # def get_absolute_file_upload_url(self):
    #     return MEDIA_URL + self.doc_file.url
