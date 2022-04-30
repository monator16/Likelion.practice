from django.shortcuts import render,redirect
from .models import Post
from datetime import datetime

# Create your views here.
def home(request):

    posts = Post.objects.all().order_by('end_date')

    for post in posts:
        now = datetime.date(datetime.now())

      
        post.d_day= ( now-post.end_date ).days

   



    return render(request, 'home.html', {'posts' : posts})


def new(request):
    if request.method =='POST':
        Post.objects.create(
            title=request.POST['title'],
            content =request.POST['content'],
            end_date =request.POST['end_date'],
        
           
        )

    return render(request,'new.html')



def detail(request,post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post': post})


def delete(request,post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')



def edit(request,post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method =='POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content =request.POST['content'],
            end_date =request.POST['end_date'],
            now_date =request.POST['now_date'],
           
        )
        return redirect('detail',post_pk)

    return render(request,'edit.html',{'post':post})
