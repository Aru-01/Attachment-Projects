from rest_framework import serializers
from product.models import Product, Category, Review


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "category"]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "product_count"]

    product_count = serializers.IntegerField(read_only=True)


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "name", "description"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)
