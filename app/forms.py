__author__ = 'adede08'

from django import forms

from app.models import JSONFile


class JSONUploadForm(forms.ModelForm):
    class Meta:
        model = JSONFile
        fields = ['file']
