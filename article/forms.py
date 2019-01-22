from django import forms


class EditForm(forms.Form):

    newTitle = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'values':'{{ article.title }}'}))
    newTextBody = forms.Textarea(attrs={'row':'6'})
