from django.conf.urls.static import static
from django.urls import path

from SHOP_REST_AJAX import settings
from .views import index, cart_add, clear_cart

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    # path('add/<int:id>', cart_add, name='cart_add'),
    path('add', cart_add, name='cart_add'),
    path('clear_cart', clear_cart, name='clear_cart'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
