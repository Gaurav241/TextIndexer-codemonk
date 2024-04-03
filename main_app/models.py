from django.db import models

class User(models.Model):
    """
    Model representing a user.
    """
    name = models.CharField(max_length=100) # Name of the user
    email = models.EmailField(unique=True) # Email of the user
    date_of_birth = models.DateField() # Date of birth of the user
    created_at = models.DateTimeField(auto_now_add=True) # The date and time on which the user was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time on which the user was last updated

class Paragraph(models.Model):
    """
    Model representing a paragraph.
    """
    content = models.TextField() # Content of the paragraph

class WordIndex(models.Model):
    """
    Model representing a word index in a paragraph.
    """
    word = models.CharField(max_length=100) # Word in the paragraph
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE) # Paragraph containing the word (foreign key)
    frequency = models.IntegerField(default=0) # Frequency of the word in the paragraph
