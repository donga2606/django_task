from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, CreateView
from .models import Category, Post
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'home.html'

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts_in_category.html'
    

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk= self.kwargs.get('pk'))
        query_set = self.category.posts_in_category.all()
        return query_set

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'update_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('posts_in_category', pk=post.category.pk)

@method_decorator(login_required, name='dispatch')
class NewPost(CreateView):
    model = Post
    fields = ['subject', 'message']
    template_name = 'new_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        post.created_user = self.request.user
        post.category = self.category
        post.save()
        return redirect('posts_in_category', pk=post.category.pk)