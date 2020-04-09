from django.shortcuts import render
from .models import post, category
from django.shortcuts import get_object_or_404
from django.http import Http404
from comment.models import comment
from django.db.models import Count
# Create your views here.
def home(request):


    if request.method == "POST":
        search = post.objects.filter(text__icontains = request.POST['search'])
        currenr_post = search.order_by('-pubDate')
        if not search:
            return render(request, 'index.html', {'error':'مطلب خاصی پیدا نشد :( اگه در موردش سوالی داری کامنت بزار و مطلب مورد نظرت رو پیشنهاد بده گل )'})
        else:
            content = {
            'post' : currenr_post
            }
            return render(request, 'index.html', content)

    else:
        current_post = post.objects.order_by('-pubDate')
        content = {
        'post' : current_post
        }
        return render(request, 'index.html', content)




def aboutMe(request):
    return render(request, 'aboutme.html')




def support(request):
    return render(request, 'payment.html')



def contact(request):
    return render(request, 'contact.html')



def postC(request, post_id):
    current_post = get_object_or_404(post, pk = post_id)
    comments     = comment.objects.filter(reply = None, post__isnull = False)
    content      = {
    'post' : current_post,
    'comments'     : comments,
    }
    return render(request, 'post.html', content)
