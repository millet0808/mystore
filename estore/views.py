from django.contrib import messages
# from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
# from django.contrib.auth.decorators import permission_required
from .models import Product
# from .forms import ProductForm


# Create your views here.
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'estore/product_index.html', {'products': products})
class ProductList(PermissionRequiredMixin, generic.ListView):
    model = Product

    def has_permission(self):
        if self.permission_required:
            return super(ProductList, self).has_permission()
        else:
            return True


class ProductDetail(generic.DetailView):
    model = Product

# @permission_required('estore.add_product')
# def product_create(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return redirect('product_index')
#     else:
#         form = ProductForm()
#     return render(request, 'estore/product_new.html', {'form': form})
class ProductCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'estore.add_product'
    model = Product
    fields = ('title', 'description', 'quantity', 'price', 'image')

    def get_success_url(self):
        messages.success(self.request, '產品已新增')
        return reverse('dashboard_product_list')


# @permission_required('estore.change_product')
# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     form = ProductForm(request.POST or None, instance=product)
#
#     if request.POST and form.is_valid():
#         form.save()
#         messages.success(request, '產品已變更')
#
#     return render(request, 'estore/product_form.html', {'form': form})
class ProductUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'estore.change_product'
    model = Product
    fields = ('title', 'description', 'quantity', 'price', 'image')

    def get_success_url(self):
        messages.success(self.request, '產品已變更')
        return reverse('dashboard_product_update', kwargs=self.kwargs)
