from django.shortcuts import render, get_object_or_404
from . models import Blog 

# Home page – list all posts
def home(request):
    posts = Blog.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'post1': posts})

# Detail page – single post
def post_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'post_detail.html', {'post': post})
