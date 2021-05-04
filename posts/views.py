from django.shortcuts import render
from .models import Post

# Create your views here.
def main_page(request):
    return render(request, 'base.html')


def about(request):
    with open('posts/texts/about_us.txt', 'r') as file:
        data=file.read()
    return render(request, 'about.html', {'data_text': data})

def contact(request):
    with open('posts/texts/about_us.txt', 'r') as file:
        data=file.read()
    return render(request, 'contact.html', {'data_text': data})


def gallery(request):
    posts = Post.objects.all()
    return render(request, 'gallery.html', {'posts': posts})





