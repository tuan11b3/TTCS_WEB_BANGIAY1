# from django.shortcuts import render
# from django.views.generic import ListView, DetailView

# from .models import Product
# from django.contrib.auth.mixins import (
#     LoginRequiredMixin,
#     PermissionRequiredMixin
# )

# # Create your views here.

# class ShoeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     model = Product
#     context_object_name = 'shoe_list'
#     template_name = 'shoes/shoe_list.html'
#     permission_required = 'shoes.special_status' # new

# def ShoeDetailView(request, pk):
#     try:
#         product = Product.objects.get(id = pk)
#     except Product.DoesNotExist:
#         print('models not exist')
#     else:
#         context = {'product': product}
#         return render(request, 'shoes/shoe_detail.html', context)
    
#     return render(request, 'error_not_found.html')

from rest_framework import generics, viewsets

from .models import Product
from .serializers import ShoesSerializer



# class ShoeListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ShoesSerializer

# class ShoeDetailView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ShoesSerializer

# class PostList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ShoesSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ShoesSerializer

class ShoesViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ShoesSerializer
