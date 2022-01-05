from django.contrib.messages.api import success
from django.db.models import fields
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # browser was looking for <app>/<model>_<viewtype>.html   in form of   blog.post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

# adds live links to usernames on homepage. Shows posts by that user. Shortcut to 404 if user does not exist
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

        # this class or more likely method needs to be tweaked to allow profile to be shown.


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):            # others must be left of UpdateView
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):        # others must be to left of DeleteView
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class SearchResultsView(ListView):
    model = Profile
    template_name = 'users/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Profile.objects.filter(
            Q(user_role__icontains=query) | Q(user_commitment_level__icontains=query)
        )
        return object_list



""" documentation

imports a shortcut 'render'
from models.py imports the Post class which defines database stuff




"""





