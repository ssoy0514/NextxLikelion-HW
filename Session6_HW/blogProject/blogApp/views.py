from unicodedata import category
from django.shortcuts import render, redirect
from .models import Article
import datetime

# Create your views here.
def new(request):
    if request.method =='POST':
        print(request.POST)
        Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = datetime.datetime.now(),
        )
        return redirect('new')

    return render(request, 'new.html')
def list(request):
    hobby_num = len(Article.objects.filter(category='hobby'))
    food_num = len(Article.objects.filter(category='food'))
    programing_num = len(Article.objects.filter(category='programing'))
    return render(request, 'list.html',{'hobby_num':hobby_num , 'food_num' : food_num, 'programing_num':programing_num})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def hobby(request):
    articles = Article.objects.filter(category='hobby')
    return render(request, 'hobby.html', {'articles':articles})

def food(request):
    articles = Article.objects.filter(category = 'food')
    return render(request, 'food.html', {'articles':articles})

def programing(request):
    articles = Article.objects.filter(category='programing')
    return render(request, 'programing.html', {'articles':articles})