from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

# Create your views here.

class ShoeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    context_object_name = 'shoe_list'
    template_name = 'shoes/shoe_list.html'
    permission_required = 'shoes.special_status' # new

def ShoeDetailView(request, pk):
    try:
        product = Product.objects.get(id = pk)
    except Product.DoesNotExist:
        print('models not exist')
    else:
        context = {'product': product}
        return render(request, 'shoes/shoe_detail.html', context)
    
    return render(request, 'error_not_found.html')