from django.shortcuts import render,redirect
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def logout(request):
    auth.logout(request)

    return redirect("list")


def login(request):
    if request.method =="POST":
        username= request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(request.GET.get("next", "/"))
        error="아이디 또는 비번이 틀립니다"
        return render(request,'registration/login.html', {'error':error})
        

    return render(request, "registration/login.html")


def signup(request):
    if request.method =="POST":
        username= request.POST['username']
        password=request.POST['password']
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error="이미 아이디가 존재합니다"
            return render(request,'registration/signup.html', {'error':error})
        new_user=User.objects.create_user(usrname=username, password=password)
        auth.login(request, new_user)
        return redirect("home")

    return render(request, "registration/signup.html")


def list(request):
    posts=Post.objects.all()
    return render(request, 'list.html',{'posts':posts})

@login_required(login_url="/registration/login")
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content= request.POST['content']
        new_post=Post.objects.create(
            title=title, content=content, author=request.user
        )
        return redirect('detail',new_post.pk)
    return render(request, 'create.html')



def edit(request, post_pk):
    post=Post.objects.filter(pk=post_pk)
    if request.method=="POST":
        post.update(
            title = request.POST['title'],
            content = request.POST['content'],

        )
        return redirect('detail', post_pk)
    return render(request, 'update.html',{'post':post[0]})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('list')
            
@login_required(login_url="/registration/login")
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    print(type(post.author),"post.author")
    post.counting +=1
    post.save()
    if request.method =='POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content= content,
            author = request.user
        )
        return redirect('detail',post_pk)
    return render(request, 'detail.html', {"post": post,"counting":post.counting})


def delete_comment(request,post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail',post_pk)
    