from .models import Post

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'clipshare/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'clipshare/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_template_names(self):
        if self.request.htmx:
            return 'clipshare/post_list.html'
        return 'clipshare/home.html'

class UserPostListView(ListView):
    model = Post
    template_name = 'clipshare/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        is_liked_ = False
        post = self.object
        if post.likes.filter(id=self.request.user.id).exists():
            is_liked_ = True
        else:
            is_liked_ = False
        context = super().get_context_data(**kwargs)
        context['is_liked'] = is_liked_
        context['total_likes'] = post.total_likes()
        return context 

def post_like(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        "total_likes": post.total_likes()
    }
    if request.htmx:
        return render(request, 'clipshare/like_section.html', context)
   
    print("hi")
    return HttpResponseRedirect(post.get_absolute_url())

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'clip_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'clip_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'clipshare/about.html', {'title': 'About'})