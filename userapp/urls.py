from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
     path("",views.Userlogin,name='userlogin'),
     path("userpanel",views.Userpanel,name='userpanel'),
     path("register", views.Userregister,name='userregister'),
     path("productlist", views.productlist, name='productlist'),

     path("userlogout", views.userlogout,name='userlogout'),
     path("add_to_cart/<int:book_id>/", views.add_to_cart,name='addtocart'),
     path("inc_item/<int:item_id>/", views.inc_quantity,name='inc_item'),
     path("dec_item/<int:item_id>/", views.dec_quantity,name='dec_item'),
     path("remove_item/<int:item_id>/", views.remove_item,name='remove_item'),
     path("clearcart", views.clearcart,name='clearcart'),
     path("cartlist", views.view_cart,name='cartlist'),

     path("checkout", views.checkout, name='checkout'),
     path("success", views.success, name='success'),
     path("cancel", views.cancel, name='cancel'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
