from django.conf.urls.static import static
from django.urls import path

from SHOP_REST_AJAX import settings
from .views import save_cart

app_name = 'save_cart'

urlpatterns = [
    path('savecart', save_cart, name='save_cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
