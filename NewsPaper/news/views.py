from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    queryset = Post.objects.filter(post_type = 'NW').order_by('-time_create')
    template_name = 'News/news_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class ArticlesList(ListView):
    queryset = Post.objects.filter(post_type = 'AR').order_by('-time_create')
    template_name = 'News/articles_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class NewsSearch(ListView):
    queryset = Post.objects.filter(post_type = 'NW').order_by('-time_create')
    template_name = 'News/news_search.html'
    context_object_name = 'postsearch'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context

class ArticlesSearch(ListView):
    queryset = Post.objects.filter(post_type = 'AR').order_by('-time_create')
    template_name = 'News/articles_search.html'
    context_object_name = 'postsearch'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    queryset = Post.objects.filter(post_type = 'NW')
    model = Post
    template_name = 'News/post.html'
    context_object_name = 'post'

class ArticlesDetail(DetailView):
    queryset = Post.objects.filter(post_type = 'AR')
    model = Post
    template_name = 'News/post.html'
    context_object_name = 'post'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'News/news_create.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NW'
        return super().form_valid(form)

class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'News/articles_create.html'
    success_url = reverse_lazy('articles_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'News/news_create.html'
    success_url = reverse_lazy('news_list')

class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'News/articles_create.html'
    success_url = reverse_lazy('articles_list')

class NewsDelete(DeleteView):
    model = Post
    template_name = 'News/news_delete.html'
    success_url = reverse_lazy('news_list')

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'News/articles_delete.html'
    success_url = reverse_lazy('articles_list')

