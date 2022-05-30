from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from django.views.generic.edit import FormMixin
from app_news.forms import CommentsForm, NewsForm
from app_news.models import News, Commentaries


class NewsListView(generic.ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()


class CreateNewsView(generic.CreateView):

    model = News
    template_name = 'app_news/news_create.html'
    fields = ['name', 'descriptions', 'flag_news']


class RegeditNewsView(generic.UpdateView):

    model = News
    template_name = 'app_news/news_regedit.html'
    context_object_name = 'regedit_form'
    form_class = NewsForm


class CommentDetailView(FormMixin, generic.DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news_detail'
    form_class = CommentsForm

    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)

        if form.is_valid():
            object = form.save(commit=False)
            object.news = self.get_object()
            object.save()
            return HttpResponseRedirect(reverse('news-detail', kwargs={'pk': self.get_object().id}))
        return render(request, 'app_news/news_detail.html', context={'form': form})

    def get_success_url(self, **kwargs):
        return reverse_lazy('news-detail', kwargs={'pk': self.get_object().id})
