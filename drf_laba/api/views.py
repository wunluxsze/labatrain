from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import *


class ProductsView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (AllowAny, )


class ProductsCreateView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminUser, )
    authentication_classes = [TokenAuthentication]


class ProductsRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permissions_classes = (IsAdminUser, )
    authentication_classes = [TokenAuthentication]


class CartView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = [TokenAuthentication]


class CartListCreateView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = [TokenAuthentication]


class CartRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminUser, )
    authentication_classes = [TokenAuthentication]


class OrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = [TokenAuthentication]


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = [TokenAuthentication]
