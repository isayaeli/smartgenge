from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from cart.models import Cart, CartItem,Order
from products.models import Product
from cart.forms import checkoutForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
 

@login_required(login_url='/login')
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user, odered=False)
        context = {
            'cart':cart
        }
        return render(request, 'cart/cart.html', context)
    except ObjectDoesNotExist:
        messages.info(request, 'You do not have an active order')
        return redirect('/')


@login_required(login_url='/login')
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item ,created = CartItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered =False
    )
    cart_qs  = Cart.objects.filter(user=request.user, odered=False)
    if cart_qs.exists():
        cart = cart_qs[0]
        if cart.items.filter(product__id=product.id).exists():
            cart_item.quantity +=1
            cart_item.save()
            messages.success(request, "The item quanity was updated.")
        else:
            messages.success(request, "The item was added to your cart.")
            cart.items.add(cart_item)
    else:
        cart = Cart.objects.create(user=request.user)
        cart.items.add(cart_item)
        messages.info(request, 'this product was added to your cart')
    return redirect('cart')

def remove_from_cart(request, id): 
    product = get_object_or_404(Product, id=id)
    cart_qs = Cart.objects.filter(
        user=request.user,
        odered=False
    )
    if cart_qs.exists():
        cart = cart_qs[0]
        if cart.items.filter(product__id=product.id).exists():
            cart_item = CartItem.objects.filter(
            product=product,
            user=request.user,
            ordered=False
            )[0]
            cart.items.remove(cart_item)
            messages.success(request, "The item was removed from your cart.")
            return redirect("cart")
        else:
            messages.info(request, "The item was not in your cart.")
            return redirect("shop")
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("shop")

def remove_single_product_from_cart(request, id): 
    product = get_object_or_404(Product, id=id)
    cart_qs = Cart.objects.filter(
        user=request.user,
        odered=False
    )
    if cart_qs.exists():
        cart = cart_qs[0]
        if cart.items.filter(product__id=product.id).exists():
            cart_item = CartItem.objects.filter(
            product=product,
            user=request.user,
            ordered=False
            )[0]
            if cart_item.quantity > 1:
                cart_item.quantity -=1
                cart_item.save()
            else:
                cart.items.remove(cart_item)
            messages.success(request, "The item was updated.")
            return redirect("cart")
        else:
            messages.info(request, "The item was not in your cart.")
            return redirect("shop")
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("shop")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        cart_items = Cart.objects.filter(user=self.request.user, odered=False)
        form = checkoutForm()
        context={
           'form':form,
           'cart_items':cart_items
        }
        return render(self.request, 'cart/checkout.html', context)
    def post(self,*args, **kwargs):
        form = checkoutForm(self.request.POST or None)
        try:
            cart = Cart.objects.get(user=self.request.user, odered=False)
            if form.is_valid():
                address = form.cleaned_data.get('address')
                second_address = form.cleaned_data.get('second_address')
                country = form.cleaned_data.get('country')
                zip_code = form.cleaned_data.get('zip_code')
                phone = form.cleaned_data.get('phone')
                email = form.cleaned_data.get('email')
                payment = form.cleaned_data.get('payment')
                order = Order(
                    user= self.request.user,
                    address= address,
                    second_address= second_address,
                    country=country,
                    zip_code=zip_code,
                    phone= phone,
                    email= email,

                )
                order.save()
                cart.odered = True
                cart.order = order
                cart.save()
                send_mail(
                    'New Order has been placed', 
                    f"Please visit your admin panel site to see order",
                    'ummasoft@gmail.com',['isayaelib@gmail.com'], fail_silently=False
                )
                if payment == 'S':
                    return redirect('payment', payment_option='stripe')
                elif payment == 'C':
                    return redirect('payment', payment_option='cash')
                else:
                    messages.warning(self.request, "Ivalid payment method")
            messages.info(self.request, "Failed checkout")
            return redirect('checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order..")
            return redirect('cart')

# class CheckOutView(View):
#     def get(self, *args, **kwargs):
#         form = checkoutForm()
#         cart_items = Cart.objects.filter(user=self.request.user, odered=False)
#         context = {
#             'form':form,
#             'cart_items':cart_items
#         }
#         return render(self.request, 'cart/checkout.html', context)

#     def post(self, *args, **kwargs):
#         form = checkoutForm(self.request.POST or None)
#         try:
#             cart = Cart.objects.get(user=self.request.user, odered=False)
#             if form.is_valid():
#                 country = form.cleaned_data.get('country')
#                 address = form.cleaned_data.get('address')
#                 second_address = form.cleaned_data.get('second_address')
#                 city = form.cleaned_data.get('city')
#                 zip_code = form.cleaned_data.get('zip_code')
#                 phone = form.cleaned_data.get('phone')
#                 # email = form.cleaned_data.get('email')
#                 payment = form.cleaned_data.get('payment')
#                 order = Order(
#                     user= self.request.user,
#                     country=country,
#                     address= address,
#                     second_address = second_address,
#                     city = city,
#                     zip_code = zip_code,
#                     phone = phone,
#                     # email=email
#                 )
#                 order.save()
#                 cart.odered=True
#                 cart.order = order
#                 cart.save()
#                 if payment == 'S':
#                     return redirect('payment', payment_option='stripe')
#                 elif payment == 'P':
#                     return redirect('payment', payment_option='paypal')
#                 elif payment == 'C':
#                     return redirect('payment', payment_option='cash')
#                 else:
#                     messages.warning(self.request, "Ivalid payment method")
#             messages.info(self.request, "Failed checkout")
#             return redirect('checkout')

#         except ObjectDoesNotExist:
#             messages.error(self.request, "You do not have an active order..")
#             return redirect('cart')


# def Checkout(request):
#     cart_items = Cart.objects.filter(user=request.user, odered=False)
#     if request.method == 'POST':
#         form = checkoutForm(request.POST )
#         order = Order()
#         if form.is_valid():
#             order.country = form.cleaned_data['country']
#             order.address = form.cleaned_data['address']
#             order.second_address = form.cleaned_data['second_address']
#             order.city = form.cleaned_data['city']
#             order.zip_code = form.cleaned_data['zip_code']
#             order.phone = form.cleaned_data['phone']
#             order.payment = form.cleaned_data['payment']
#             order.save()
#             # cart_items.odered = True
#             if payment == 'S':
#                 return redirect('payment', payment_option='stripe')
#             elif payment == 'P':
#                 return redirect('payment', payment_option='paypal')
#             elif payment == 'C':
#                 return redirect('payment', payment_option='cash')
#             else:
#                 messages.warning(self.request, "Ivalid payment method")
#         messages.info(request, "Failed checkout")
#         return redirect('checkout')

#     form = checkoutForm()
#     context = {
#         'cart_items':cart_items,
#         'form':form
#     }
#     return render(request, 'cart/checkout.html', context)


def payment(request, payment_option):
    order = Order.objects.filter(user=request.user).order_by('-id')
    cart_items = Cart.objects.filter(user=request.user, odered=True).order_by('-id')
    context = {
     'order':order,
     'cart_items':cart_items
    }
    return render(request, 'cart/payment.html', context)

               


















