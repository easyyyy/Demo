import time

from django.shortcuts import render,redirect

# Create your views here.
from login import forms, models


def signup(request):
    message = '你的信息将会被保存.'
    if request.method == 'POST':
        signupform = forms.SignUpForm(request.POST)

        if signupform.is_valid():
            username = signupform.cleaned_data['username']
            useremail = signupform.cleaned_data['useremail']
            userpassword = signupform.cleaned_data['userpassword']

            same_user_name = models.User.objects.filter(username=username)
            if same_user_name:
                message = '该用户已存在，请重新选择用户名。'
                return render(request,'login/sign-up.html',locals())
            same_user_email = models.User.objects.filter(useremail=useremail)
            if same_user_email:
                message = '该邮箱已被注册，请使用其他邮箱。'
                return render(request,'login/sign-up.html',locals())

            new_user = models.User()
            new_user.username = username
            new_user.useremail = useremail
            new_user.userpassword = userpassword
            new_user.save()
            return redirect('/signin/')
    signupform = forms.SignUpForm()
    return render(request,'login/sign-up.html',locals())


def signin(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == 'POST':
        signinform = forms.SignInForm(request.POST)
        if signinform.is_valid():
            username = signinform.cleaned_data['username']
            userpassword = signinform.cleaned_data['userpassword']
            try:
                user = models.User.objects.get(username=username)
            except:
                message = '用户名或密码错误！'
                return render(request,'login/sign-in.html',locals())

            if user.userpassword == userpassword:
                request.session['is_login'] = True
                request.session['user_name'] = user.username
                return redirect('/index/')
            else:
                message = '用户名或密码错误！'
                return render(request, 'login/sign-in.html', locals())


    signinform = forms.SignInForm()
    return render(request,'login/sign-in.html',locals())

def index(request):

    nowtime = time.strftime('%B  %d,%Y')
    return render(request,'index/index.html',locals())

def forgetpassword(request):

    return render(request, 'login/forget.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')