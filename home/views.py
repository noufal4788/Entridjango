from django.shortcuts import render

# Create your views here.
from  . models import Author, Post

def post_list(request):
    posts = Post.objects.all()
    authors = Author.objects.all()
    return render(request,'home.html',{'posts': posts,'authors':authors})