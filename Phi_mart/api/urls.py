from django.urls import include, path

urlpatterns = [
    path("products/", include("product.product_urls")),
    path("categories/", include("product.category_urls")),
]
