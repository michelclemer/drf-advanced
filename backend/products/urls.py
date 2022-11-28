from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/', views.product_mixin_view, name='product-detail'),
    path('delete/<int:pk>', views.product_delete_view,),
    path('update/<int:pk>/', views.product_detail_view,name='product-edit'),



]
