from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
# router = SimpleRouter()
router.register('product', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls
# urlpatterns = [
# path('', include(router.urls))
# path('products/', views.ProductList.as_view()),
# path('products/<int:pk>', views.ProductDetail.as_view()),
# path('collections/', views.CollectionList.as_view()),
# path('collections/<int:pk>', views.CollectionDetail.as_view(),
#      name='collection-detail'),
# ]
