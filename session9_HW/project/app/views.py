from django.shortcuts import render,redirect
from .models import Post,Comment

# Create your views here.

def list(request):
    posts=Post.objects.all()
    return render(request, 'list.html',{'posts':posts})

def create(request):
    if request.method == 'POST':
        new_post=Post.objects.create(
            title = request.POST['title'],
            author= request.POST['author'],
            content= request.POST['content']
        )
        return redirect('detail',new_post.pk)
    return render(request, 'create.html')



def edit(request, post_pk):
    post=Post.objects.filter(pk=post_pk)
    if request.method=="POST":
        post.update(
            title = request.POST['title'],
            author = request.POST['author'],
            content = request.POST['content'],

        )
        return redirect('detail', post_pk)
    return render(request, 'update.html',{'post':post[0]})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('list')
            

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.counting +=1
    post.save()

    if request.method =='POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content= content
        )
        return redirect('detail',post_pk)
    return render(request, 'detail.html', {"post": post,"counting":post.counting})


def delete_comment(request,post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail',post_pk)
    