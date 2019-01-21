from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50,label='用户名',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'姓名','id':'name'}))
    useremail = forms.EmailField(label='电子邮箱',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Email','type':'text'}))
    userpassword = forms.CharField(max_length=50,label='密码',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'密码'}))


class SignInForm(forms.Form):
    username = forms.CharField(max_length=50,label='用户名',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'姓名','id':'name'}))
    userpassword = forms.CharField(max_length=50, label='密码',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))