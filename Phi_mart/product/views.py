from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from product.models import Product, Category
from product import serializers


# Create your views here.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = serializers.ProductSerializers

    # def get_queryset(self):
    #     return Product.objects.select_related("category").all()

    # def get_serializer_class(self):
    #     return serializers.ProductSerializers


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializers
    lookup_field = "id"


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = serializers.CategorySerializers


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = serializers.CategorySerializers
    lookup_field = "id"

