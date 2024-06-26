import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Userprofile, Logins, Carts, Cartitems
from adminpanelapp.models import Book


# Create your views here.

def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = Logins.objects.filter(username=username, password=password).exists()

        try:
            if user is not None:
                user_details = Logins.objects.get(username=username, password=password)
                user_name = user_details.username
                usertype = user_details.usertype
                userid = user_details.id
                if usertype == 'user':
                    request.session['username'] = user_name
                    request.session['usertype'] = usertype
                    request.session['userid'] = userid
                    return redirect('userpanel')
                elif usertype == 'admin':
                    request.session['username'] = user_name
                    request.session['usertype'] = usertype
                    return redirect('admindashboard')
                else:
                    messages.error(request, "invalid username/password")
        except:
            messages.error(request, "Invalid Role")
    return render(request, 'login.html')


def Userregister(request):
    login_table = Logins()
    userprofile = Userprofile()

    if request.method == 'POST':
        userprofile.username = request.POST['username']
        userprofile.password = request.POST['password']
        userprofile.confirm_password = request.POST['cpassword']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.usertype = 'user'

        if request.POST['password'] == request.POST['cpassword']:
            userprofile.save()
            login_table.save()
            messages.info(request, "User Registration Successful")
            return redirect('userlogin')
        else:
            messages.info(request, "Password does not match")
            return redirect('userregister')
    return render(request, 'register.html')


def Userpanel(request):
    return render(request, 'users/userdashboard.html')


def productlist(request):
    books = Book.objects.all()
    return render(request, 'users/productlist.html', {'books': books})


def userlogout(request):
    logout(request)
    return redirect('userlogin')


def add_to_cart(request, book_id):
    user_id = request.session.get('userid')
    user_details = Logins.objects.get(id=user_id)
    productid = book_id

    book = Book.objects.get(id=productid)

    cart_obj, created = Carts.objects.get_or_create(user=user_details)
    itemexist = Cartitems.objects.filter(cart=cart_obj, book=book).exists()
    if itemexist:
        itemsobj = Cartitems.objects.get(cart=cart_obj, book=book)
        itemsobj.quantity += 1
        itemsobj.save()
    else:
        cartitem = Cartitems.objects.create(cart=cart_obj, book=book)
    return redirect('cartlist')


def view_cart(request):
    user_id = request.session.get('userid', 'Guest')

    user_details = Logins.objects.get(id=user_id)
    carts = Carts.objects.get(user=user_details)
    cart_items = carts.cartitems_set.all()
    cart_item = Cartitems.objects.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    total_items = cart_items.count()
    items = Cartitems.objects.filter(cart=carts)


    context = {
        'carts': carts,
        'items':cart_items,
        'cart_items':cart_items,
        'cart_item': cart_item,
        'total_price':total_price,
        'total_items':total_items
    }
    return render(request, 'users/cart.html', context)




def inc_quantity(request, item_id):
    cart_item = Cartitems.objects.get(id=item_id)

    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cartlist')


def dec_quantity(request, item_id):
    cart_item = Cartitems.objects.get(id=item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cartlist')


def remove_item(request, item_id):
    user_id = request.session.get('userid', 'Guest')
    user_details = Logins.objects.get(id=user_id)
    try:
        cart_item = Cartitems.objects.get(id=item_id)
        carts = Carts.objects.get(user=user_details)
        cart_item.delete()
        carts.delete
    except:
        pass
    return redirect('cartlist')


def clearcart(request):
    user_id = request.session.get('userid', 'Guest')
    user_details = Logins.objects.get(id=user_id)
    try:
        cart_item = Cartitems.objects.all()
        carts = Carts.objects.all()
        cart_item.delete()
        carts.delete
    except:
        pass

    return redirect('cartlist')


def checkout(request):
    cart_items = Cartitems.objects.all()

    if cart_items:
        stripe.api_key = settings.STRIPE_SECRET_KEY

        if request.method == 'POST':

            line_items = []

            for cart_item in cart_items:
                if cart_item.book:
                    line_item = {
                        'price_data':{
                            'currency':'INR',
                            'unit_amount':int(cart_item.book.price * 100),
                            'product_data':{
                                'name':cart_item.book.title
                            }
                        },
                        'quantity':1
                    }
                    line_items.append(line_item)

            if line_item:
                checkout = stripe.checkout.Session.create(
                    payment_method_types = ['card'],
                    line_items = line_items,
                    mode ='payment',
                    success_url=request.build_absolute_uri(reverse('success')),
                    cancel_url = request.build_absolute_uri(reverse('cancel'))
                )

            return redirect(checkout.url,code=303)


def success(request):
    cart_items = Cartitems.objects.all()

    for cart_item in cart_items:
        product = cart_item.book

        if product.quantity > cart_item.quantity:
            product.quantity -= cart_item.quantity
            product.save()

    cart_items.delete()

    return  render(request,'users/success.html')

def cancel(request):
    return render(request, 'users/cancel.html')


