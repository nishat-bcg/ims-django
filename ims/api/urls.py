from unicodedata import name
from django.urls import path

from api.controllers import suppliers
from api.controllers import categories
from api.controllers.customerGroups import CustomerGroupController
from api.controllers.products import ProductController, SingleProductController
from api.controllers.customer import CustomerController, CustomersController
from api.controllers.productOrder import ProductOrdersController, ProductOrderController

urlpatterns = [
    path('suppliers/', suppliers.SupplierController.as_view(), name='suppliers'),
    path('categories/', categories.CategoryController.as_view(), name='categories'),
    path('customer-group/', CustomerGroupController.as_view(), name='customer_group'),

    path('products/', ProductController.as_view(), name='products'),
    path('products/<int:pk>', SingleProductController.as_view(), name='products'),

    path('customers/', CustomersController.as_view(), name='customers'),
    path('customers/<int:pk>', CustomerController.as_view(), name='customers'),

    path('product-order/', ProductOrdersController.as_view(), name='product-order'),
    path('product-order/<int:pk>', ProductOrderController.as_view(), name='product-order'),
]