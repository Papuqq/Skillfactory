from datetime import datetime

from django.urls import reverse_lazy

from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)


class PostList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.filterset = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_loaded'] = datetime.now().time()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')