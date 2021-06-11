from django.db import models
from django.urls import reverse


# HomeWork 7: The model for creating personal data
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, unique=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('update_person', args=[str(self.id)])

    def __str__(self):
        return self.first_name
