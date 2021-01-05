"""mapocho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import *
from cart.views import *
from blog.views import *
from users.views import *
from contacts.views import *
from about.views import about
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('product/<int:id>/', single_product, name='product'),
    
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove-from-cart'),
    path('remove/<int:id>/', remove_single_product_from_cart, name='remove'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('blogs/', blog, name='blogs'),
    path('blog/<int:id>/', single_blog, name='single_blog'),
    path('delete-comment/<int:id>/', comment_delete, name='delete_comment'),
    path('edit-comment/<int:pk>/', CommentEditView.as_view(), name='edit_comment'),

    path('wish-list/', wishlist, name='wishlist'),
    path('add-to-wish-list/<int:id>', add_to_wishlist, name='add_wishlist'),
    path('remove-from-wish-list/<int:id>', remove_from_wish_list, name='remove_wishlist'),
    path('remove/<int:id>', remove_single, name='remove_single'),

    path('login/', login_request, name='login' ),
    path('logout/', logout_request, name='logout' ),
    path('register/', register, name='register' ),

    path('contacts/', contact, name='contact'),

    path('about/', about, name='about'),
    path('payment/<payment_option>/', payment, name='payment'),

    path('fruits/', fruits, name='fruits'),
    path('juice/', juice, name='juice'),
    path('vegitable/', vegetable, name='vegetable'),
    path('dried/', dried, name='dried'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('confirm/', confirm_account, name='confirm'),
    path('confirm-link/', confirm_link , name='confirm-link'),


     path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    
]




if settings.DEBUG:
    urlpatterns += static(
         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
