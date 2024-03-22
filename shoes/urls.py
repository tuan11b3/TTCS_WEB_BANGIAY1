from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import ShoesViewSet


# urlpatterns = [
#     # path('', ShoeListView.as_view(), name='shoe_list'),
#     # path('<int:pk>/', ShoeDetailView.as_view(), name='shoe_detail'),
#     # path('create/', PostList.as_view(), name='cre_products_list'),
#     # path('create/<int:pk>/', PostDetail.as_view(), name='cre_product_detail'),
    
# ]
router = SimpleRouter()
router.register('', ShoesViewSet, basename='shoe_list')

urlpatterns = router.urls