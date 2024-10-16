from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from iphone.models import Iphone
from macbook.models import Macbook
from ipad.models import Ipad
from laptop.models import Laptop


def index(request):
    return render(request,"index.html")


CATEGORY_MODEL_MAP = {
    'Ipad': Ipad,
    'Iphone':Iphone,
    'Macbook':Macbook,
    'Laptop':Laptop
}

def product_detail(request, category, pslug):
   
    model = CATEGORY_MODEL_MAP.get(category)
    
    if not model:
        # If the category is not found in the mapping, you can raise a 404 error
        return render(request, '404.html')  # Or use a more appropriate response

    # Fetch the product detail based on the slug
    detail = get_object_or_404(model, slug=pslug)
    
    data = {
        'detail': detail
    }
    return render(request, "product_detail.html", data)

def laptop(request):
    laptopdata = Laptop.objects.all()
    data = {
        'laptopdata':laptopdata
    }
    return render(request,"laptop.html",data)

def iphone(request):
    iphonedata = Iphone.objects.all()
    data = {
        'iphonedata':iphonedata
    }
    return render(request,"iphone.html",data)

def macbook(request):
    macbookdata = Macbook.objects.all()
    data = {
        'macbookdata':macbookdata
    }
    
    return render(request,"macbook.html",data)

def ipad(request):
    ipaddata = Ipad.objects.all()
    data = {
        'ipaddata':ipaddata
    }
    return render(request,"ipad.html",data)
