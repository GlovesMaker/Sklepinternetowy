from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.
from cart.forms import CartAddProductForm


def error_404(request):
        data = {}
        return render(request,'apka/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'apka/error_500.html', data)

def koszt(request):
    return render(request, 'apka/koszt.html')

def zwrot(request):
    return render(request, 'apka/zwrot.html')

def regulamin(request):
    return render(request, 'apka/regulamin.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'apka/product/list.html', {'category': category, 'categories': categories, 'products': products})
                                                    
                                       
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'apka/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})





