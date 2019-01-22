from django.shortcuts import render, redirect

# Create your views here.
import login.views
from article import models, forms


def detail(request,articleId):

    article = models.Article.objects.get(id=articleId)

    return render(request,'index/detail.html',locals())


def edit(request,articleId):
    article = models.Article.objects.get(id=articleId)
    if request.method == 'POST':
        newtitle = request.POST.get('newtitle')
        newtext = request.POST.get('newtext')
        models.Article.objects.filter(id=articleId).update(title=newtitle,textbody=newtext)
        return redirect('/index/')
    else:
        print('error')
    return render(request,'index/edit.html',locals())