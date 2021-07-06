from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product
from django.http import JsonResponse


def index(request):
    products = Product.objects.all()
    count = check_count(request)
    return render(request, "index.html", context={'products': products, 'count': count})

# def cart_add(request, id):
#     request.session['cart'].append({'id': id, 'quantity': 1})
#     request.session.modified = True
#     check_count(request)
#     return redirect('shop:index')

def cart_add(request):
    if request.method == "POST" and request.is_ajax():
        id = request.POST.get('id', None)
        request.session['cart'].append({'id': id, 'quantity': 1})
        request.session.modified = True
        count = check_count(request)
        print(request.session['cart'])
        return JsonResponse({'id': id, 'count': count})
    return JsonResponse({'message': 'Error'})

def check_count(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    count = 0
    for i in request.session['cart']:
        count += 1
    return count

def clear_cart(request):
    if request.method == "POST" and request.is_ajax():
        request.session['cart'] = []
        count = 0
        # return redirect('shop:index')
    return JsonResponse({'count': count})

# def add_oredr(request):
#     if request.method == 'POST':
#         addorder = OrderCreateForm(request.POST)
#         if addorder.is_valid():
#             addorder.save()
#         return redirect('shop:index')
#     else:
#         addorder = OrderCreateForm()
#     return render(request, 'admin/add-product.html', {'form': addorder})

