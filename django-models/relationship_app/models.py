from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)  # Optional field
    nationality = models.CharField(max_length=50, null=True, blank=True)  # Optional field

    def __str__(self):
        return self.name
