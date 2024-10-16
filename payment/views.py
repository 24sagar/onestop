
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Order
from cart.models import Cart, CartItem
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import logging
from iphone.models import Iphone  
from ipad.models import Ipad  
from laptop.models import Laptop  
from macbook.models import Macbook

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


# Logger setup for debugging
logger = logging.getLogger(__name__)


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    # If the cart is empty, redirect back with a message
    if not cart_items:
        messages.error(request, 'Your cart is empty!')
        return redirect('view_cart')

    context = {
        'cart_products': cart_items,
        'total_price': total_price,
    }

    return render(request, 'checkout.html', context)



@login_required
def place_order(request):
    if request.method == "POST":
        # Retrieve address from form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # Validate form fields
        if not all([first_name, last_name, email, address, city, country, zip_code, phone]):
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('checkout')

        # Check for cart items
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()
        if not cart_items:
            messages.error(request, 'Your cart is empty!')
            return redirect('view_cart')

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

        total_amount = sum([product['total_price'] for product in cart_products])

        
        amount_in_paisa = int(total_amount * 100)  # Convert to paisa

        # Create Razorpay order
        try:
            razorpay_order = razorpay_client.order.create({
                'amount': amount_in_paisa,
                'currency': 'INR',
                'payment_capture': '1'
            })
        except razorpay.errors.RazorpayError as e:
            logger.error(f"Error creating Razorpay order: {e}")
            messages.error(request, 'There was an error processing your payment. Please try again.')
            return redirect('checkout')

        # Create Order in the database
        try:
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
                city=city,
                country=country,
                zip_code=zip_code,
                phone=phone,
                amount=total_amount,
                razorpay_order_id=razorpay_order['id'],
            )
            logger.debug(f"Created order: {order.id} with Razorpay order ID: {order.razorpay_order_id}")
        except Exception as e:
            logger.error(f"Error creating Order instance: {e}")
            messages.error(request, 'There was an error creating your order. Please try again.')
            return redirect('checkout')

        # Pass Razorpay details to the payment page
        context = {
            'order': order,
            'cart_items': cart_items,
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'total_amount': total_amount,
        }

        return render(request, 'payment_page.html', context)
    else:
        return redirect('checkout')

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        # Razorpay will send a POST request with payment details after payment
        payment_data = request.POST
        razorpay_order_id = payment_data.get('razorpay_order_id')
        razorpay_payment_id = payment_data.get('razorpay_payment_id')
        razorpay_signature = payment_data.get('razorpay_signature')

        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            # Verify the signature
            razorpay_client.utility.verify_payment_signature(params_dict)

            # If signature is valid, fetch the order and mark as paid
            order = Order.objects.get(razorpay_order_id=razorpay_order_id)
            order.razorpay_payment_id = razorpay_payment_id
            order.status = 'Paid'
            order.save()

            # Clear the user's cart
            CartItem.objects.filter(cart__user=order.user).delete()

            # Log success and redirect to success page
            logger.info(f"Payment successful for order: {order.id}")
            return JsonResponse({'status': 'Payment successful'})
        except razorpay.errors.SignatureVerificationError as e:
            # Handle failed signature verification
            logger.error(f"Signature verification failed: {e}")
            return JsonResponse({'status': 'Payment failed: Signature Verification Error'}, status=400)
        except Order.DoesNotExist:
            logger.error(f"Order with Razorpay Order ID {razorpay_order_id} does not exist.")
            return JsonResponse({'status': 'Payment failed: Order does not exist'}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error during payment callback: {e}")
            return JsonResponse({'status': 'Payment failed: Unexpected Error'}, status=400)

    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def payment_success(request):
    return render(request, 'payment_success.html')
