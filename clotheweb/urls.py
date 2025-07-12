from django.urls import path
from . import views


urlpatterns = [
    path('homec/', views.homec, name='homec'),  # This is the url for home function
    path('loginc/', views.loginc, name='loginc'),  # This is the url for login function
    path('logout/', views.logoutc, name='logoutc'),
    path('registerc/', views.registerc, name='registerc'),  # This is the url for register function
    path('cartc/',views.cartc, name='cartc'),
    path('aboutc/', views.aboutc, name='aboutc'),  # This is the url for about function
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order/place/', views.place_order, name='place_order'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orderc/', views.orderc, name='orderc'),  # This is the url for order function
    path('confirm_order/', views.confirm_order, name='confirm_order'),  # This is the url for confirm order function
    path('deliveryc/', views.deliveryc, name='deliveryc'),
    path('paymentc/', views.paymentc, name='paymentc'),
    path('payment/confirm/', views.payment_confirm, name='payment_confirm'),
    path('contact/', views.contactc, name='contactc'),


    #path('place_order_all/', views.place_order_all, name='place_order_all'),  # optional
       
]