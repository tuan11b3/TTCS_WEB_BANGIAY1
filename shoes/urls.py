from django.urls import path


from .views import ShoeListView, ShoeDetailView


urlpatterns = [
    path('', ShoeListView.as_view(), name='shoe_list'),
    path('<int:pk>', ShoeDetailView, name='shoe_detail'),
]