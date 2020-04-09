from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import postC



urlpatterns = [
    path('<int:post_id>', postC, name = "post"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
