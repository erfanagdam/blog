from django.db import models
from blog import models as blogModel
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from jdatetime import datetime as jdate



class comment(models.Model):
    post  = models.ForeignKey(blogModel.post, null=True, blank = True, on_delete = models.CASCADE)
    user  = models.ForeignKey(User, on_delete = models.CASCADE)
    text  = models.TextField(max_length = 500)
    date  = jmodels.jDateField(auto_now_add = True)
    reply = models.ForeignKey('comment', null=True, blank = True, related_name='replies', on_delete = models.CASCADE)
