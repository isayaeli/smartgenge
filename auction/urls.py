from django.urls import path
from . import views
urlpatterns = [
    path('auction', views.auction, name='auction'),
    path('bid/<int:id>', views.bid, name='bid'),
    path('add_bid/', views.add_bid, name='add_bid')
] 