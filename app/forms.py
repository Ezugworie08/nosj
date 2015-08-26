__author__ = 'adede08'

from django import forms

from app.models import JSONFile


# def verify_json(file):
#     with open(file) as f:
#         print("print pussy")
#         data = json.loads(f.read())


class JSONUploadForm(forms.ModelForm):
    class Meta:
        model = JSONFile
        fields = ['file']
