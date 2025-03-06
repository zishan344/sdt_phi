from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet

from rest_framework_nested import routers

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='category')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')

product_router.register('reviews',ReviewViewSet,basename='product-review') 
# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('',include(product_router.urls))
    # path('products/',include('product.product_urls')),
    # path('categories/',include('product.category_urls'))
]