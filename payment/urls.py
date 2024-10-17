from django.urls import path
from . import views

urlpatterns = [
    # path('checkout/', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),
    path('payment_callback/', views.payment_callback, name='payment_callback'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('order_history/', views.order_history, name='order_history'),
    path('recent_order/', views.recent_order, name='recent_order'),
]