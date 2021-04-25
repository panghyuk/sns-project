from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request,'main/mainpage.html')

def show(request):
    return render(request, 'main/show.html')

def who(request):
    return render(request,'main/who.html')

def what(request):
    return render(request,'main/what.html')

def future(request):
    return render(request,'main/future.html') 