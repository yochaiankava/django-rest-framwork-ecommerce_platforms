from django.urls import path
from . import views
urlpatterns = [
    # product - for list of products and create product.
    path('product/', views.products, name="products"), 
    path('product/<id>', views.product_detail, name="product_detail"), 
    path('category/', views.categories, name="categories"),    
    path('category/<id>', views.category_detail, name="category_detail"), 
    # path('cart/', views.cart, name="cart"),    
    # path('cart/<id>', views.cart_detail, name="cart_detail"), 
] 