from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View
from app_news.forms import NewsForm
from app_news.models import News


class NewsFormView(generic.ListView):

    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_form'
    queryset = News.objects.all()


class NewsCreateFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/news_create.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_news/news_list.html', context={'news_form': news_form})