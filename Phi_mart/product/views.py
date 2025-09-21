from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.models import Product, Category, Review
from product import serializers
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.pagination import DefaultPagination

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ["category_id"]
    filterset_class = ProductFilter
    search_fields = ["name", "description"]
    ordering_fields = ["price", "updated_at"]
    pagination_class = DefaultPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = serializers.CategorySerializers


class ReviewViewSet(ModelViewSet):
    serializer_class = serializers.ReviewSerializers

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
