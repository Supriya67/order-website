from django.urls import path
from .views import Products,Index,Carts,Checkout,Order
urlpatterns=[
    path('',Index.as_view(), name="index"),
    path('product', Products.as_view(), name="product"),
    path('carts', Carts.as_view(), name="carts"),
    path('check-out', Checkout.as_view(), name="checkout"),
path('orders', Order.as_view(), name="order"),
]