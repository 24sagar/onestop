from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'phone', 'amount', 'status', 'razorpay_order_id', 'razorpay_payment_id', 'created_at')
    list_filter = ('status', 'country', 'city', 'created_at')
    search_fields = ('user__username', 'razorpay_order_id', 'razorpay_payment_id', 'email', 'first_name', 'last_name', 'phone')
    readonly_fields = ('razorpay_order_id', 'razorpay_payment_id', 'created_at')

admin.site.register(Order, OrderAdmin)