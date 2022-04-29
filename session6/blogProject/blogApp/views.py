from unicodedata import category
from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            
                    
        )
        return redirect('list')

    return render(request, 'new.html')


def list(request):
    hobbycount= len(Article.objects.filter(category ="hobby"))
    foodcount= len(Article.objects.filter(category ="food"))
    programmingcount= len(Article.objects.filter(category ="programming"))
    ordered_articles = Article.objects.order_by('title')
    return render(request, 'list.html',{'hobbycount':hobbycount, 'foodcount':foodcount, 'programmingcount':programmingcount,'ordered_articles':ordered_articles})


def category(request,category_id):

    articles= Article.objects.filter(category=category_id)
    return render(request, 'category.html', {'articles':articles})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})


