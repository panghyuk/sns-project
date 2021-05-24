from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def showmain(request):
    posts = Post.objects.all()
    return render(request,'main/mainpage.html',{'posts':posts})

def show(request):
    return render(request, 'main/show.html')

def who(request):
    return render(request,'main/who.html')

def what(request):
    return render(request,'main/what.html')

def future(request):
    return render(request,'main/future.html') 

def detail(request,id):
    post = get_object_or_404(Post,pk = id)
    return render(request,'main/detail.html',{'post':post})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail',new_post.id)