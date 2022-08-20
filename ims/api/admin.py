from django.contrib import admin

# Register your models here.
from api.models.supplier import Supplier
from api.models.category import Category
from api.models.customerGroup import CustomerGroup
from api.models.product import Product
from api.models.customer import Customer
from api.models.productOrder import ProductOrder

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    empty_value_display = '?'
    list_display = ['id','name','address','phone','email']

@admin.register(Category)
class SupplierAdmin(admin.ModelAdmin):
    empty_value_display = '?'
    list_display = ['id','name','description',]

@admin.register(CustomerGroup)
class SupplierAdmin(admin.ModelAdmin):
    empty_value_display = '?'
    list_display = ['id','name']


@admin.register(Product)
class SupplierAdmin(admin.ModelAdmin):
    empty_value_display = '?'
    list_display = ['id','name', 'price', 'supplier', 'category']

@admin.register(Customer)
class SupplierAdmin(admin.ModelAdmin):
    empty_value_display = '?'
    list_display = ['id','first_name', 'last_name', 'address', 'phone', 'email', 'group']

@admin.register(ProductOrder)
class SupplierAdmin(admin.ModelAdmin):
    empty_value_display = '?'
    list_display = ['id','customer', 'product', 'order_discount', 'total_price', 'order_date']