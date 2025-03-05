from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet, ProductImageViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewset

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='category')
router.register('carts', CartViewSet, basename="carts")
router.register('orders', OrderViewset, basename='orders')

cart_router = routers.NestedDefaultRouter(
    router, 'carts', lookup='cart'
)

cart_router.register('items', CartItemViewSet, basename='cart-items')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
product_router.register('images',ProductImageViewSet, basename = 'product-images')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls')),
    # path('products/', include('product.product_urls')),
    # path('categories/', include('product.category_urls'))
]