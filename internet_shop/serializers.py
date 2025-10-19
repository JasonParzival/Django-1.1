from rest_framework import serializers

from internet_shop.models import Product
from internet_shop.models import Category
from internet_shop.models import Customer
from internet_shop.models import Order
from internet_shop.models import OrderDetail

# №2
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

# №1
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'quantity', 'category']
        
# №3    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'phone_number', 'email']
        
# №4
class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'date', 'status', 'customer']

# №5     
class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderDetail
        fields = ['id', 'order', 'product', 'quantity']