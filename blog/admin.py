from django.contrib import admin
from django.db import models
from .models import post, category
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from pagedown.widgets import AdminPagedownWidget





class postAdmin(admin.ModelAdmin):
    list_filter = (
        ('pubDate', JDateFieldListFilter),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(post, postAdmin)
admin.site.register(category)
