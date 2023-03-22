from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ProductsView.as_view()),
    path('items/<int:pk>/', ProductsCreateView.as_view()),
    path('items/<int:pk>/', ProductsRetrieve.as_view()),
    path('cart/', CartView.as_view()),
    path('cart/<int:pk>/', CartListCreateView.as_view()),
    path('cart/<int:pk>/', CartRetrieveView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', OrderListCreateView.as_view()),
 ]
