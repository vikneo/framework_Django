from django import forms
from app_news.models import Commentaries, News


class NewsForm(forms.ModelForm):

    name = forms.CharField(label='Заголовок', widget=forms.Textarea(attrs={'rows': '3'}))
    descriptions = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'rows': '11'}))

    class Meta:
        model = News
        fields = '__all__'


class CommentsForm(forms.ModelForm):

    comment = forms.CharField(label='Текст комментария', widget=forms.Textarea)

    class Meta:
        model = Commentaries
        fields = ('user_name', 'comment',)
