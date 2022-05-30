from django import forms

from app_news.models import News, Comments


class NewsForm(forms.ModelForm):

    article = forms.CharField(label='Описание', widget=forms.Textarea)

    class Meta:
        model = News
        fields = '__all__'
