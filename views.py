# from typing import Any
# from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Product,Category,Profile,Reviews,Cart,CartItem
from django.contrib.auth.decorators import login_required
from .form import ProfileForm,ReviewForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
# from django.http import HttpResponse
# from .models import News,Category,Profile,Comments
# from django.contrib.auth.models import User,auth

# from .form import CategoryForm
# from .form import NewsForm, ProfileForm,CommentForm
# from django.contrib.auth.decorators import login_required

# from django.views import View
# from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView





# Create your views here.


def homefn(request):
    
    p=Product.objects.all()
    c=Category.objects.all()
    png=Paginator(p,10)

    page_num=request.GET.get("page")

    
    page_obj=png.get_page(page_num)

    # if request.user.is_authenticated:
    #     cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    #     print(cart)
    
    return render(request,'home.html',{'category':c,'product':page_obj})

def registertionfn(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        em=request.POST['email']
        us=request.POST['usname']
        p1=request.POST['password1']
        p2=request.POST['password2']
        
        if p1==p2:
            if User.objects.filter(username=us).exists():

                messages.error(request,'username already taken ')
                return redirect ('/register')
                # return HttpResponse('username already taken')
            
            elif User.objects.filter(email=em).exists():

                messages.error(request,'email already taken ')
                return redirect ('/register')
                # return HttpResponse('email already taken')
            
            else:
        
                u=User.objects.create_user(username=us,email=em,first_name=fn,last_name=ln,password=p1)
                u.save()
                # return HttpResponse('saved')
                messages.success(request,'register successfully.. ')
                return redirect ('/login')
        
        else:
            messages.error(request,'password not matching... ')
            return redirect ('/register')
            # return HttpResponse('password is not same')

    
    else:

        return render(request,'registration.html')
    

def loginfn (request):
    if request.method=='POST':
        us=request.POST['usname']
        p1=request.POST['password1']

        user=auth.authenticate(username=us,password=p1)
                               
        if user:
            auth.login(request,user)

            return redirect ('/')
        
        else:
            # return HttpResponse('invalid credentials..')
            messages.error(request,'invalid credentials.. ')
            return redirect ('/login')
        
    else:
        return render(request,'login.html')
    
def categoryfn(request,c_id):
    c=Category.objects.all()

    p=Product.objects.filter(ctry=c_id)
    return render(request,'home.html',{'product':p,'category':c})

def profilefn(request):
    x=Profile.objects.filter(user=request.user.id)
    if x:

        p=Product.objects.filter(user=request.user.id)

        return render(request,'profile.html',{"product":p})
    
    else:
        return redirect('/profileform')
    

@login_required(login_url='/login')
def Profileform(request):
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.save()
            # form.save()
            return redirect('/')
        
    else:

        p=ProfileForm()

        return render(request,'profileform.html',{'form':p})
    
def logoutfn (request):
    auth.logout(request)

    return redirect ('/login')

def viewfn(request,p_id):
    
    if request.method=="POST":
        p=Product.objects.get(id=p_id)
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.post=p
            # abc.user=p_id
            abc.save()
            return redirect(f'/viewpage/{p_id}')
    else:
        c=Category.objects.all()
        p=Product.objects.get(id=p_id)
        v=Reviews.objects.filter(post=p_id)
        e=ReviewForm()
        
        return render(request,'viewpage.html',{'product':p ,'form':e, 'review':v ,'category':c})
    
def searchfn(request):
    item=request.GET['ab']
    prt=Product.objects.filter(Q(name__icontains=item) | Q(details__icontains=item))

    return render(request,'home.html',{'product':prt})

# def addtocart(request):
#     data = json.loads(request.body)
#     product_id = data["id"]
#     product = Product.objects.get(id=product_id)

#     if request.user.is_authenticated:
#         cart, created= Cart.objects.get_or_create(user=request.user, completed=False)
#         cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
#         cartitem.quantity += 1
#         cartitem.save()

#         num_of_items = cart.num_of_items

#         print(cartitem)
#         return JsonResponse(num_of_items, safe=False)
    

# def cart(request):
#     cart = None
#     cartitems = []

#     if request.user.is_authenticated:
#         cart, created = cart.cartitems.all()
#         print(cart)
#     return render(request, 'cart.html',{"cart":cart, "items":cartitems})


