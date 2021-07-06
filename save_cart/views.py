from django.shortcuts import render

from product.models import Product
from product.views import check_count




def save_cart(request):
    products = Product.objects.all()
    count = check_count(request)
    return render(request, "save_cart.html", context={'products': products, 'count': count})
