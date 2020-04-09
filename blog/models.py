from django.db import models
from jdatetime import date as jdate
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class category(models.Model):
    title = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 20)
    def __str__(self):
        return '{} *:|:* {}'.format(self.title, self.subject)



class post(models.Model):
    title = models.CharField(max_length = 60)
    text = RichTextField()
    pubDate = jmodels.jDateField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ManyToManyField(category)
    def __str__(self):
        return '{} *:|:* {}'.format(self.title, self.author)
