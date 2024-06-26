from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
     #path("",views.index),
     path("userslist", views.userlist, name='userslist'),
     path("userscreate", views.createusers, name='userscreate'),
     path("editusers/<int:user_id>/", views.updateusers),
     path("deleteuser/<int:user_id>/", views.deleteuser),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
