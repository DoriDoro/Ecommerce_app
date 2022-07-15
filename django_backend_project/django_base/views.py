# get info from: https://www.django-rest-framework.org/api-guide/views/
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# create all routes:
@api_view(['GET'])
def get_routes(request):
    routes = [
        'api/products/',
        'api/products/create/',

        'api/products/upload/',

        'api/products/<id>/reviews/',

        'api/products/top/',
        'api/products/<id>/',

        'api/products/delete/<id>/',
        'api/products/<update>/<id>/',
    ]
    return Response(routes)


# get all the products information:
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    # serializer: wraps our model(s) and tern it into JSON format:
    serializer = ProductSerializer(products, many=True)  # many=True means we will serialze many not just one
    return Response(serializer.data)


# get one product information:
@api_view(['GET'])
def get_product(request, pk):  # pk is a primary key (id)
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)  # many=False because just one product
    return Response(serializer.data)
