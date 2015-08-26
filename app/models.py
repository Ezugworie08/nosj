from django.db import models

# Create your models here.


class JSONFile(models.Model):
    file = models.FileField(upload_to='json/%Y/%m/%d')

    def __str__(self):
        return self.file.url
