"""
URL configuration for OneStopSolutions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from OneStopSolutions import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('laptop/',views.laptop,name='laptop'),
    path('iphone/',views.iphone,name='iphone'),
    path('macbook/',views.macbook,name='macbook'),
    path('ipad/',views.ipad,name='ipad'),
    path('product_detail/<category>/<pslug>/',views.product_detail,name='product_detail'),
    path('',include('auth_app.urls')),
    path('',include('cart.urls')),
    path('',include('payment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)