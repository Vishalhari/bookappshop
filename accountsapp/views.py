from django.shortcuts import render, redirect
from userapp.models import Userprofile,Logins
from .forms import UserForm, UserFormcreate


# Create your views here.


def userlist(request):
    userlist = Logins.objects.all()

    return render(request,'admin/listusers.html',{'users':userlist})


def createusers(request):
    if request.method == 'POST':
        form = UserFormcreate(request.POST)

        if form.is_valid():
            form.save()
            return redirect('userslist')
    else:
        form = UserFormcreate()
    return render(request,'admin/createuser.html',{'form':form})

def deleteuser(request,user_id):
    users = Logins.objects.get(id=user_id)

    if request.method == 'POST':
        users.delete()
        return redirect('userslist')
    else:
        return render(request,'admin/deleteuser.html',{'users':users})








def updateusers(request,user_id):
    users = Logins.objects.get(id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST,instance=users)
        if form.is_valid():
            form.save()

            return redirect('userslist')
    else:
        form = UserForm(instance=users)

    return render(request,'admin/updateusers.html',{'form':form})




