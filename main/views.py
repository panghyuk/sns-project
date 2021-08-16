from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# 2. 사용할 모듈 불러오기
# 2-1 POST 형식의 HTTP 통신만 받기
from django.views.decorators.http import require_POST
# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답
from django.http import HttpResponse
# 2-3 딕셔너리를 json 형식으로 바꾸기 위해
import json

# Create your views here.
def showmain(request):
    posts = Post.objects.all()
    return render(request,'main/mainpage.html',{'posts':posts})

def posts(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'main/posts.html', {'posts': posts})

def who(request):
    return render(request,'main/who.html')

def what(request):
    return render(request,'main/what.html')

def future(request):
    return render(request,'main/future.html') 

def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request,'main/detail.html',{'post':post, 'comments':all_comments})

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

# comment
def create_comment(request,post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post,pk = post_id)
    new_comment.save()
    return redirect('main:detail', post_id)

def edit_comment(request,comment_id):
    edit_comment = Comment.objects.get(id = comment_id)
    return render(request,'main/edit_comment.html',{'comment':edit_comment})

def update_comment(request,comment_id):
    update_comment = get_object_or_404(Comment, pk = comment_id)
    update_comment.writer = request.user
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('main:detail',update_comment.post.id)

def delete_comment(request,comment_id):
    delete_comment = get_object_or_404(Comment,pk = comment_id)
    delete_comment.delete()
    return redirect('main:detail', delete_comment.post.id)

# 3. like_toggle 함수 작성하기
@require_POST
@login_required
def like_toggle(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post_like,post_like_created = Like.objects.get_or_create(user = request.user, post = post)

    if not post_like_created:
        post_like.delete()
        result = 'like_cancel'
    else:
        result = 'like'

    context = {
        "like_count":post.like_count,
        "result":result
    }
    return HttpResponse(json.dumps(context),content_type='application/json')

def dislike_toggle(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post_dislike,post_dislike_created = Dislike.objects.get_or_create(user = request.user, post = post)

    if not post_dislike_created:
        post_dislike.delete()
        result = 'dislike_cancel'
    else:
        result = 'dislike'

    context = {
        "dislike_count":post.dislike_count,
        "result":result
    }

    return HttpResponse(json.dumps(context),content_type='application/json')