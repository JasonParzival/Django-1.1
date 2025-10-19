"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from internet_shop import views


from rest_framework.routers import DefaultRouter

from internet_shop.api import ProductsViewset
from internet_shop.api import CategoriesViewset
from internet_shop.api import CustomersViewset
from internet_shop.api import OrdersViewset
from internet_shop.api import OrderDetailsViewset

router = DefaultRouter()
router.register("products", ProductsViewset, basename="product")
router.register("categories", CategoriesViewset, basename="category")
router.register("customers", CustomersViewset, basename="customer")
router.register("orders", OrdersViewset, basename="order")
router.register("orderDetails", OrderDetailsViewset, basename="orderDetail")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowProductsView.as_view()),
    path('api/', include(router.urls)),
]
