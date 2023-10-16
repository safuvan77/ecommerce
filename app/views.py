
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *





def register(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        pword1=request.POST.get('password1')
        pword2=request.POST.get('password2')
        
        if (pword1 != pword2):
            messages.info(request,'incorrect password')
        else:
            User.objects.create_user(
                username=uname,
                password=pword2,
            ) 
            messages.success(request,'Success')
            return redirect('login')
    return render(request,'register.html')
    
def all_login(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        user=authenticate(username=uname,password=pword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'incorrect password')
    return render(request,'login.html')
    

def all_logout(request):
    logout(request)
    return redirect('login') 


def home(request):
    if request.user.is_staff == False:
        products=Product.objects.all()
        return render(request,"home.html",context={'product':products})
    else:
        products=Product.objects.all()
        return render(request,"admin_home.html",context={'product':products})                
 
            
def product_add(request):
    if request.method == 'POST':
        p_name = request.POST['name']
        p_image = request.FILES['image']
        p_price = request.POST['price']
        p_description =request.POST['description']
        Product.objects.create(
            name=p_name, 
            image=p_image,
            price=p_price,
            description=p_description,
            status=False,
            )
        return redirect('home')
    return render(request, 'add_product.html')   



def product_update(request,id):
    single_product=Product.objects.get(id=id)

    if request.method=='POST':
        p_name=request.POST.get('name')
        p_image=request.FILES.get('image')
        p_price=request.POST.get('price')
        p_description =request.POST.get('description')

        if p_name:
            single_product.name = p_name

        if p_image:    
            single_product.image = p_image

        if p_price:    
            single_product.price = p_price

        if p_description:
            single_product.description = p_description

        single_product.save()
        return redirect('home')
    return render(request,'update.html',{'var':single_product})

def product_status(request,id):
    single_product=Product.objects.get(id=id)
    if single_product:
        single_product.status = not single_product.status
        single_product.save()
    return redirect('home')



def product_delete(request,id):
    single_product=Product.objects.get(id=id)
    single_product.delete()
    return redirect('home')



def product_view(request,id):
    single_product=Product.objects.get(id=id)
    return render(request,'product_view.html',{'prod':single_product})
           
    
def addcart(request,id):
    user=User.objects.get(username=request.user.username)
    if user:
        single_product=Product.objects.get(id=id)
        check=Cart.objects.filter(fk_product=single_product,fk_user=user).first()
        if check:
            check.quantity += 1
            check.sub_total = (check.quantity * check.fk_product.price)
            check.save()
            return redirect("cart")
        else:
            Cart.objects.create(
                fk_user=user,
                fk_product=single_product,
                quantity=1,
                sub_total=single_product.price
                )
            
        return redirect ("cart")
    
    
def cartview(request):
    cartitem=Cart.objects.filter(fk_user=request.user).all().order_by("-id")
    total = 0
    count=0
    for i in cartitem:
        count += i.quantity
        total += i.sub_total
    context={
        'cartitem':cartitem,
        'total':total,
        'count':count,
        }
    return render (request,'cart.html',context)

        
def plus(request,id):
    item=Cart.objects.get(id=id)
    item.quantity += 1
    item.sub_total = (item.quantity * item.fk_product.price)
    item.save()
    return redirect("cart")

def minus(request,id):
    item=Cart.objects.get(id=id)
    if item.quantity > 0:
        item.quantity -= 1
        item.sub_total = (item.quantity * item.fk_product.price)
        item.save()
    else:
        item.delete()
    return redirect("cart")

def itemdelete(request,id):
    item=Cart.objects.get(id=id)
    item.delete()
    return redirect("cart")




         