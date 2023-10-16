from django.urls import path
from .views import *


urlpatterns = [
   
    path('register/',register,name='register'),
    path('',all_login,name='login'),
    path('logout/',all_logout,name='logout'),
    path('home/',home, name='home'),
  
    
    path('add_product',product_add, name='add_product'),
    path('update/<int:id>/',product_update, name='update'),
    path('status/<int:id>/',product_status, name='status'),
    path('delete/<int:id>/',product_delete, name='delete'),
    
    path('product_view/<int:id>/',product_view, name='product_view'),
    
 
   
    path('addcart/<int:id>/',addcart,name='cartview'),
    path('cart/',cartview,name='cart'), 
    path('plus/<int:id>/',plus,name="plus"),
    path('minus/<int:id>/',minus,name="minus"),
    path('itemdelete/<int:id>/',itemdelete,name="itemdelete"),
    
    
]