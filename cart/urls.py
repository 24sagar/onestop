

from django.urls import path
from . import views

urlpatterns = [
    # The slug will come from the specific product model (iPhone, iPad, etc.)
    path('add-to-cart/<str:category>/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]
