from django.shortcuts import render, get_object_or_404, redirect
from main.models import *
from .models import User

# Create your views here.

def follow(request,id):
    user = request.user
    followed_user = get_object_or_404(User,pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)

def mypage(request, id):
    user=get_object_or_404(User,pk=id)
    context={
        'user':user,
        'posts':Post.objects.filter(writer=user).order_by('-pub_date'),
        'followings':user.profile.followings.all(),
        'followers':user.profile.followers.all(),
    }
    return render(request,'users/mypage.html', context)