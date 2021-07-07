from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from django.http import JsonResponse

from save_cart.models import Save_cart


def index(request):
    products = Product.objects.all()
    count = check_count(request)
    return render(request, "index.html", context={'products': products, 'count': count})

# def cart_add(request):
#     if request.method == "POST":
#         id = request.POST.get('id', None)
#         token = request.POST.get('csrfmiddlewaretoken', None)
#         print(token)
#         request.session['cart'].append({'id': id, 'quantity': 1})
#         request.session.modified = True
#         check_count(request)
#         cart_session = request.session['cart']
#         edit_cart = Save_cart.objects.filter(token=token).first()
#         edit_cart2 = Save_cart.objects.all()
#         for i in edit_cart2:
#             if i.token == token:
#                 print(i.token)
#                 edit_cart.session_cart = cart_session
#                 edit_cart.save()
#             else:
#                 Save_cart.objects.create(token=token, session_cart=cart_session)
#
#
#     return redirect('product:index')

def cart_add(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.is_ajax():
            # token = request.POST.get('csrfmiddlewaretoken', None)
            quantity = request.POST.get('quantity', None)
            token = 'USERs42dgklasnflankgjnkjadsnagdsgas'
            id = request.POST.get('id', None)
            list = Save_cart.objects.all()
            test = count_products(list, token)
            request.session['cart'].append({'id': id, 'quantity': quantity})
            request.session.modified = True
            count = check_count(request)
            if test == token:
                object = Save_cart.objects.filter(token=token).first()
                object.session_cart = request.session['cart']
                object.save()
            else:
                create = Save_cart.objects.create(token=token, session_cart=request.session['cart'])
                create.save()
            return JsonResponse({'id': id, 'count': count})
        return JsonResponse({'message': 'Error'})
    else:
        if request.method == "POST" and request.is_ajax():
            # token = request.POST.get('csrfmiddlewaretoken', None)
            quantity = request.POST.get('quantity', None)
            token = 'GUESTs42dgklasnflankgjnkjadsnagdsgas'
            id = request.POST.get('id', None)
            list = Save_cart.objects.all()
            test = count_products(list, token)
            request.session['cart'].append({'id': id, 'quantity': quantity})
            request.session.modified = True
            count = check_count(request)
            if test == token:
                object = Save_cart.objects.filter(token=token).first()
                object.session_cart = request.session['cart']
                object.save()
            else:
                create = Save_cart.objects.create(token=token, session_cart=request.session['cart'])
                create.save()
            return JsonResponse({'id': id, 'count': count})
        return JsonResponse({'message': 'Error'})

def count_products(list, token):
    for i in list:
        if i.token == token:
            return i.token




# def handle_cart(request):
#     tables = []
#     for item in request.session['cart']:
#         table = Save_cart.query.filter_by(id=item['id']).first()
#         tables.append({'id_product': table.id,
#                        'quantity': table.quantity,
#                        })
#     return tables


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

