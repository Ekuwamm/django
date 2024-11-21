from django.shortcuts import render

from.models import Post
# Create your views here.
from django.contrib.auth.decorators import login_required


def Posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/Posts_list.html', {"posts":posts})


def Post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/Post_page.html', {"post":post})


@login_required(login_url="/users/mylogin/")
def post_new(request):
    return render(request, 'posts/post_new.html')