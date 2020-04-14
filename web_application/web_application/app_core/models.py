from __future__ import unicode_literals
from django.db import models
from django import forms
from django.forms import ClearableFileInput

# Enabling the ability to delete files 
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Resume(models.Model):
    # Allow user to upload a PDF resume
    pdf = models.FileField('Upload Resume', upload_to = 'media/')
    # Define an industry specification with bound max length of 50 chars
    industry = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.industry
   
    # Possible error here, need to fix! 
    def delete(self, *args, **kwargs):
        # Deleting pdf  
        self.pdf.delete()
        # Now able to delete industry string
        self.industry = ''
        super().delete(*args, **kwargs)
