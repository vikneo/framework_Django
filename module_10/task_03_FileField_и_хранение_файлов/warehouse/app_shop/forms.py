from django import forms
from app_shop.models import File


class UploadFileForm(forms.Form):
    file = forms.FileField()


class DocumentFile(forms.ModelForm):

    class Meta:
        model = File
        fields = ('description', 'file',)
