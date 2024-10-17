
from .models import Order

def recent_order_processor(request):
    if request.user.is_authenticated:
        recent_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
        return {'recent_order': recent_order}
    return {'recent_order': None}
