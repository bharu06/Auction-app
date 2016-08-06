from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from auction.models import *
from django import forms

class bidForm(forms.Form):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class ItemForm(forms.Form):
    name = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))

def myitems_view(request):
    uname=request.user.username
    items_list=items.objects.filter(username=uname)
    context={}
    print items_list
    context={'items_list':items_list}
    context['username'] = request.user.username
    return render(request,'auction/myitems.html',context)

def delete_view(request,id):
    item=items.objects.filter(id=id)
    items.objects.filter(id=id).delete()
    print item
    return HttpResponseRedirect('/auction/myitems/')

def home_view(request):
    username_check= request.GET.get('username_check', None)
    login_check=request.GET.get('login_check',None)
    context = {'username_check': '','login_check': ''}
    if login_check:
        context['login_check']=login_check
    if username_check :
        context['username_check']='Username Already Exists'
    return render(request, 'auction/home.html',context)

def bids_view(req,id):
    context={}
    bids_list=bids.objects.filter(item_id=id)
    context['bids_list']=bids_list
    return render(req, 'auction/viewbids.html', context)

@login_required(login_url='/auction/?login_check=Not Logged In')
def items_view(req):
    context={}
    context['username']= req.user.username
    items_list=items.objects.all()
    context['items_list']=items_list
    return render(req,'auction/items.html',context)


def itemdetail_view(req,id):
    item = items.objects.get(id=id)
    if req.method=='GET':
        context={}
        context['item'] = item
        return render(req, 'auction/itemdetail.html', context)
    else:
        itemobject=bids(username=req.user.username,item_id=item,price=req.POST['price'])
        if bids.objects.filter(item_id=item).exists() and bids.objects.filter(username=req.user.username):
            bidobj=bids.objects.get(item_id=item)

            bidobj.price=req.POST['price']
            bidobj.save()
            print "exists update"
        else :
            itemobject.save()
            print "add"
        return HttpResponseRedirect('/auction/items/')



@login_required(login_url='/auction/?login_check=Not Logged In')
def additems_view(request):
    if request.method=='GET':
        context={}
        context['username']= request.user.username
        form=ItemForm()
        context['form']=form
        return render(request,'auction/additem.html',context)
    else:
        #print request.POST
        #print request.FILES
        #Saving the File
        itemformInstance=ItemForm(request.POST,request.FILES)
        if(itemformInstance.is_valid()):
            print itemformInstance.cleaned_data
            itemInstance=items()
            itemInstance.name=itemformInstance.cleaned_data['name']
            itemInstance.Description = itemformInstance.cleaned_data['Description']
            itemInstance.username=request.user.username
            itemInstance.price = itemformInstance.cleaned_data['price']
            itemInstance.image = itemformInstance.cleaned_data['image']
            print request.user.username
            print itemInstance
            itemInstance.save()
            #indaka url rale ? anduke IDE vadakordu , chupika pothe ledu anukuntam
            #itemInstance.image.url
            return HttpResponseRedirect('/auction/myitems/')
        else:
            return HttpResponse("Wrong Fields Data")

def signup(request):
    if User.objects.filter(username=request.POST['username']).exists():
        return HttpResponseRedirect('/auction/?username_check=failed')
    else :
        user = User.objects.create_user(request.POST['username'], request.POST['Email'], request.POST['Password'],first_name=request.POST['firstname'], last_name=request.POST['lastname'])
        user.save()
        return HttpResponseRedirect('/auction/items/')

def login_view(request):
    user=authenticate(username=request.POST['username'],password=request.POST['Password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/auction/items/')
        else:
            return HttpResponse("account disbled")
    else :
        return HttpResponseRedirect('/auction/?login_check=Invalid Credentials')