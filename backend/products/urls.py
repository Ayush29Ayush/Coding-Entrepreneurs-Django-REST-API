from django.urls import path

from . import views 

urlpatterns = [
    # path('', views.product_create_view),
    path('', views.product_list_create_view),
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
    path('<int:pk>/', views.product_detail_view)
]