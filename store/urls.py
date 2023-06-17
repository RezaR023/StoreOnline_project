from django.urls import path, include
from . import views
# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
# router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

product_router = routers.NestedDefaultRouter(
    parent_router=router, parent_prefix='products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')

# colleciton_router = routers.NestedDefaultRouter(
#     router, 'collections', lookup='collection')
# colleciton_router.register(
#     'reviews', views.ReviewViewSet, basename='collection-reviews')

# urlpatterns = router.urls + product_router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    #    path('', include(colleciton_router.urls)),
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>', views.ProductDetail.as_view()),
    # path('collections/', views.CollectionList.as_view()),
    # path('collections/<int:pk>', views.CollectionDetail.as_view(),
    #      name='collection-detail'),
]
