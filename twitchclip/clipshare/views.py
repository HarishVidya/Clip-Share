from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Harish',
        'title': 'Insane Trickshot',
        'content': '360 no scope',
        'date': 'January 4, 2023'
    },
    {
        'author': 'John',
        'title': 'Fortnite Clip',
        'content': '1v4 clutch',
        'date': 'December 12, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'clipshare/home.html', context)

def about(request):
    return render(request, 'clipshare/about.html', {'title': 'About'})