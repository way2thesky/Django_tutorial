from django.db import models


class Quote(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    quote = models.CharField(max_length=300)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.quote


class Author(models.Model):
    """Model representing an author."""
    author_title = models.CharField(max_length=100)
    author_born_date = models.DateField(null=True, blank=True)
    author_born_location = models.CharField(max_length=100)
    author_description = models.TextField()

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.author_title
