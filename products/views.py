from django.shortcuts import render, redirect, get_object_or_404
from products.models import *
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from about.models import Testimonial

def home(request):
    products = Product.objects.all()[:8]
    testimon = Testimonial.objects.all()
    context ={
        'products':products,
        'testimon':testimon
    }
    return render(request, 'products/index.html', context)

def shop(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/shop.html', context)

def single_product(request, id):
    details = Product.objects.get(id=id)
    products = Product.objects.all()[:4]
    item = CartItem.objects.filter(id=id)
    context = {
        'details':details,
        'products':products,
        'item':item
    }
    return render(request, 'products/product-single.html', context)
    
@login_required(login_url='login')
def wishlist(request):
    wish_list = Wishlist.objects.get(user=request.user)
    context = {
        'list':wish_list
    }
    return render(request, 'products/wishlist.html', context)

@login_required(login_url='login')
def add_to_wishlist(request,id):
    product = get_object_or_404(Product, id=id)
    wish_item, created = wishlist_item.objects.get_or_create(
        user = request.user,
        product= product
    )
    wish_qs = Wishlist.objects.filter(user=request.user)
    if wish_qs.exists():
        wish = wish_qs[0]
        if wish.items.filter(product__id=product.id).exists():
            wish_item.quantity += 1
            wish_item.save()
        else:
            wish.items.add(wish_item) 
    else:
        wish = Wishlist.objects.create(user=request.user)
        wish.items.add(wish_item)
    return redirect('wishlist')

@login_required(login_url='login')
def remove_from_wish_list(request, id):
    product = get_object_or_404(Product, id=id)
    wish_qs = Wishlist.objects.filter(user=request.user)
    if wish_qs.exists():
        wish = wish_qs[0]
        if wish.items.filter(product__id=product.id).exists():
            wish_item = wishlist_item.objects.filter(user=request.user,product=product)[0]
            wish.items.remove(wish_item)
            return redirect('wishlist')
        else:
            return redirect('wishlist')
    else:
        return redirect('wishlist')
@login_required(login_url='login')
def remove_single(request, id):
    product = get_object_or_404(Product, id=id)
    wish_qs = Wishlist.objects.filter(user=request.user)
    if wish_qs.exists():
        wish = wish_qs[0]
        if wish.items.filter(product__id=product.id).exists():
            wish_item = wishlist_item.objects.filter(user=request.user, product=product)[0]
            if wish_item.quantity > 1:
                wish_item.quantity -= 1
                wish_item.save()
            else:
                wish.items.remove(wish_item)
            return redirect('wishlist')
        else:
            return redirect('wishlist')
    else:
        return redirect('wishlist')


def fruits(request):
    fruits = Product.objects.filter(category='fruit')
    context = {
        'fruits':fruits
    }
    return render(request, 'products/fruits.html', context)


def juice(request):
    juice = Product.objects.filter(category='juice')
    context = {
        'juice':juice
    }
    return render(request, 'products/juice.html', context)


def vegetable(request):
    vegetable = Product.objects.filter(category='vegitable')
    context = {
        'vegetable':vegetable
    }
    return render(request, 'products/vegitable.html', context)

def dried(request):
    dried = Product.objects.filter(category='dried')
    context = {
        'dried':dried
    }
    return render(request, 'products/dried.html', context)

