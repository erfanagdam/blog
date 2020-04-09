from django.shortcuts import render
from .models import comment
from django.db.models import Count

def commentSys(request):
    comments     = comment.objects.filter(reply = None, post = None)
    commentCount = comment.objects.filter(replies = None, post = None).aggregate(Count('text'))
    countAll     = comment.objects.aggregate(Count('text'))
    replyCount   = countAll['text__count'] - commentCount['text__count']
    content      = {
    'comments'     : comments,
    'commentCount' : commentCount['text__count'],
    'replyCount'   : replyCount,
    }
    return render(request, 'comment.html', content)
