from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=3000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'notes'