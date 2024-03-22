from django.urls import path


from .views import ShoeListView, ShoeDetailView, PostList, PostDetail


urlpatterns = [
    path('', ShoeListView.as_view(), name='shoe_list'),
    path('<int:pk>/', ShoeDetailView.as_view(), name='shoe_detail'),
    path('create/', PostList.as_view(), name='cre_products_list'),
    path('create/<int:pk>/', PostDetail.as_view(), name='cre_product_detail'),
]