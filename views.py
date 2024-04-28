from django.shortcuts import render,HttpResponseRedirect
from .form import studentRegister
from.models import User
# Create your views here.

# This function is for Add and show Data
def add_show(request):
    if request.method=="POST":
        fm=studentRegister(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            store=User(name=nm, email=em, password=pw)
            store.save()
            fm=studentRegister()
    else:
        fm=studentRegister()
    stu=User.objects.all()
    return render(request,'enrolltempla/addandshow.html',{'f':fm,'st':stu})

# this function is for delete 

def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
# this function for update/Edit
def update_date(request,id):
    if request.method=="POST":
        p=User.objects.get(pk=id)
        fm=studentRegister(request.POST,instance=p)
        if fm.is_valid():
            fm.save()
    else:
        p=User.objects.get(pk=id)
        fm=studentRegister(instance=p)
    return render(request,'enrolltempla/update.html',{'f':fm})
   




        



