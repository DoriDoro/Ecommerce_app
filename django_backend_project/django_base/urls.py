from django.urls import path
# import all views
from . import views


urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('products/', views.get_products, name='products'),
    path('products/<str:pk>', views.get_product, name='product'),
]
