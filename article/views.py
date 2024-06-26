from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from article.forms import ArticleManagerForm
from article.models import Article
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleManagerForm
    success_url = reverse_lazy('article:articles')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("article.change_article"):
            return ArticleManagerForm
        raise PermissionDenied


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleManagerForm
    success_url = reverse_lazy('article:articles')

    def get_success_url(self):
        return reverse('article:article_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("article.change_article"):
            return ArticleManagerForm
        raise PermissionDenied


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article:articles')


class ArticleListView(ListView):
    model = Article
    template_name = 'article/articles_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


def toggle_activity(request, pk):
    article_item = get_object_or_404(Article, pk=pk)
    if article_item.is_published:
        article_item.is_published = False
    else:
        article_item.is_published = True

    article_item.save()
    return redirect(reverse('article:articles'))
