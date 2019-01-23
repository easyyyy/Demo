import time

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


def add(request):
    if request.method=="POST":
        title = request.POST.get('title')
        textbody = request.POST.get('text')
        texthead = textbody[:50]
        author_name = request.session.get('user_name')
        author_email = request.session.get('user_email')
        author = login.models.User.objects.get(useremail=author_email)
        date = time.strftime("%B  %d,%Y")
        newAritcle = models.Article()
        newAritcle.title = title
        newAritcle.textbody = textbody
        newAritcle.texthead = texthead
        newAritcle.author = author
        newAritcle.date = date
        newAritcle.save()

        return redirect('/index/')
    return render(request,'index/add.html')


def delete(request,articleId):
    models.Article.objects.get(id=articleId).delete()
    return redirect('/index/')