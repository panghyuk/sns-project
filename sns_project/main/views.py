from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def showmain(request):
    posts = Post.objects.all()
    return render(request,'main/mainpage.html',{'posts':posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})

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
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail',new_post.id)

def edit(request,id):
    edit_post = Post.objects.get(id=id)
    return render(request,'main/edit.html',{'post':edit_post})

def update(request,id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('main:detail',update_post.id)

def delete(request,id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:posts')