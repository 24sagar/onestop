from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem,UserAddress
from .forms import UserAddressForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from iphone.models import Iphone  
from ipad.models import Ipad  
from laptop.models import Laptop  
from macbook.models import Macbook
import razorpay
from django.conf import settings

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def add_to_cart(request, category, product_slug):
    # Determine which model to use based on the category
    if category == 'Iphone':
        product = get_object_or_404(Iphone, slug=product_slug)
    elif category == 'Ipad':
        product = get_object_or_404(Ipad, slug=product_slug)
    elif category == 'Laptop':
        product = get_object_or_404(Laptop, slug=product_slug)
    elif category == 'Macbook':
        product = get_object_or_404(Macbook, slug=product_slug)
    else:
        return redirect('view_cart')  # If category is invalid, return to the cart

    # Create or retrieve the cart for the logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Add or update the cart item
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_slug=product_slug, product_category=category)
    if not created:
        # If the item is already in the cart, increment the quantity
        cart_item.quantity += 1
    else:
        # If the item was just created, set the quantity to 1 (already default)
        cart_item.quantity = 1

    cart_item.save()

    return redirect('view_cart')  # Redirect to the cart page



@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()

    # Handle address form
    try:
        address = UserAddress.objects.get(user=request.user)
    except UserAddress.DoesNotExist:
        address = None

    if request.method == 'POST':
        form = UserAddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'Your address has been updated!')
            return redirect('view_cart') 
    else:
        form = UserAddressForm(instance=address)

    # Retrieve product details based on the category and slug
    cart_products = []
    for item in cart_items:
        if item.product_category == 'Iphone':
            product = get_object_or_404(Iphone, slug=item.product_slug)
        elif item.product_category == 'Ipad':
            product = get_object_or_404(Ipad, slug=item.product_slug)
        elif item.product_category == 'Laptop':
            product = get_object_or_404(Laptop, slug=item.product_slug)
        elif item.product_category == 'Macbook':
            product = get_object_or_404(Macbook, slug=item.product_slug)
        
        cart_products.append({
            'product': product,
            'name': product.name, 
            'quantity': item.quantity,
            'total_price': product.price * item.quantity,
        })

    total_price = sum([product['total_price'] for product in cart_products])
    if total_price < 1:
        messages.error(request, "Your cart is empty or the total amount is too low to proceed.")
        return redirect('/')

    amount_in_paisa = int(total_price * 100)

    # Create Razorpay Order
    razorpay_order = razorpay_client.order.create({
        'amount': amount_in_paisa, 'currency': 'INR', 'payment_capture': '1'
    })

    context = {
        'cart_products': cart_products,
        'total_price': total_price,
        'form': form,
        'address': address,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID
    }

    return render(request, 'checkout.html',context)


@login_required
def clear_cart(request):
    cart = Cart.objects.get(user=request.user)  
    CartItem.objects.filter(cart=cart).delete()  
    return redirect('view_cart')  