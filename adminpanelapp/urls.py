from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
     #path("",views.index),
     path("booklist", views.Listbook, name='booklist'),
     path("userdashboard", views.Listbook,name='userdashboard'),
     path("admindashboard", views.Listbook, name='admindashboard'),
     path("addbook/",views.createBook,name='addbook'),
     path("addauthor/",views.CreateAuthor,name='addauthor'),

    path("listauthor", views.Listauthor,name='listauthor'),
    path("editauthor/<int:author_id>/", views.UpdateAuthor),
    path("deleteauthor/<int:author_id>/", views.deleteauthor),

    path("editbook/<int:book_id>/", views.UpdateBook),
    path("showbook/<int:book_id>/", views.Bookdetails),

    # path("updatebook/<int:book_id>/", views.UpdateBook),
    path("deletebook/<int:book_id>/", views.deletebook),
    path("search/", views.Search_book,name='search')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
