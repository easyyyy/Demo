from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=50)
    useremail = models.EmailField(primary_key=True)
    userpassword = models.CharField(max_length=50)