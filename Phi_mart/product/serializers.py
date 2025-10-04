from rest_framework import serializers
from product.models import Product, Category, Review
from django.contrib.auth import get_user_model


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "category"]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "product_count"]

    product_count = serializers.IntegerField(read_only=True)


class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name="get_user_name")

    class Meta:
        model = get_user_model()
        fields = ["id", "name"]

    def get_user_name(self, obj):
        return obj.get_full_name()


class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name="get_user")

    class Meta:
        model = Review
        fields = ["id", "user", "product", "ratings", "comment"]
        read_only_fields = ["user", "product"]

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)
