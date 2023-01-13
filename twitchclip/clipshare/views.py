from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'Harish',
        'title': 'Insane Trickshot',
        'content': '360 no scope',
        'date_posted': 'January 4, 2023',
        'clip_link': 'ssdfkjsdfsd'
    },
    {
        'author': 'John',
        'title': 'Fortnite Clip',
        'content': '1v4 clutch',
        'date_posted': 'December 12, 2022',
        'clip_link': 'ssdfkjsdfsd'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'clipshare/home.html', context)

def about(request):
    return render(request, 'clipshare/about.html', {'title': 'About'})