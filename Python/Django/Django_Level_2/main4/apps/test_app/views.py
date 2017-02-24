from django.shortcuts import render, redirect
from . models import Blog, Comment
# Create your views here.
def index(req):
    context = {
    "blogs": Blog.objects.all()
    # select * from Blog
    }
    print context['blogs']
    return render(req, 'test_app/index.html', context)
def blogs(req):
    # using ORM
    Blog.objects.create(title=req.POST['title'], blog=req.POST['blog'])
    # insert into blogs (title, blog, created_at, updated_at) values (title, blog, NOW(), NOW())
    return redirect('/')
def comments(req, id):
    print WALLYYYYYY
    blog = Blog.objects.get(id = id)
    Comment.objects.create(comment=req.POST['comment'], blog=blog)
    return redirect('/')
