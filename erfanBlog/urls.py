from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from blog import views
from account import views as accountViews
from comment import views as commentViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('signup', accountViews.signup, name = "signup"),
    path('login', accountViews.login, name = "login"),
    path('logout', accountViews.logout, name = "logout"),
    path('post/', include('blog.urls')),
    path('comment', commentViews.commentSys, name = "comment"),
    path('about', views.aboutMe, name = "aboutMe"),
    path('support', views.support, name = "support"),
    path('contact', views.contact, name = "contact"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
