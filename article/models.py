from django.db import models

# Create your models here.
from django.urls import reverse

import login.models


class Article(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(login.models.User,on_delete=models.CASCADE)
    textbody = models.TextField()
    texthead = models.TextField()
    date = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('detail')
