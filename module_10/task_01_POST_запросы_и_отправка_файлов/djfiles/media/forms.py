from django import forms


class FileUploadForm(forms.Form):

    title = forms.CharField(max_length=60)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class ReadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
