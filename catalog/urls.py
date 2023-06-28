from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', views.product, name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #все файлы, загружаемые пользователем, статические
