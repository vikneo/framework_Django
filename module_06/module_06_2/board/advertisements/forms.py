from django import forms


class AdvertisementForms(forms.Form):
    title = forms.CharField()
    descriptions = forms.CharField()
    price = forms.FloatField()
