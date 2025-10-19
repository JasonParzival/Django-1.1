from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from internet_shop.models import Product
from internet_shop.serializers import ProductSerializer

from internet_shop.models import Category
from internet_shop.serializers import CategorySerializer

from internet_shop.models import Customer
from internet_shop.serializers import CustomerSerializer

from internet_shop.models import Order
from internet_shop.serializers import OrderSerializer

from internet_shop.models import OrderDetail
from internet_shop.serializers import OrderDetailSerializer

class ProductsViewset(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoriesViewset(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CustomersViewset(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class OrdersViewset(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetailsViewset(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer