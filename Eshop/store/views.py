from django.shortcuts import render
from .models.product import Product

def index(request):
    context = {
        'products': Product.get_all_product(),
    }
    print(context)
    return render(request, 'store/index.html',context=context)
# Create your views here.
