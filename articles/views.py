from django.shortcuts import render
from . import models

# Create your views here.

articles = models.Article.objects.all().order_by('date')
args = {'articles' : articles}

def articles_list(request):
    return render(request , 'articles/articleslist.html', args)
