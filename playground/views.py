from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem
# Create your views here.


def say_hello(request):
    queryset1 = Product.objects.filter(unit_price__range=(10, 30))
    queryset2 = Product.objects.filter(
        ~Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    # queryset33 and queryset3 have the same results.
    queryset3 = Product.objects.filter(
        id=F('orderitem__product_id')).distinct().order_by('title')
    queryset33 = Product.objects.filter(id__in=OrderItem.objects.values(
        'product_id').distinct()).order_by('title')
    # for prod in query_set:
    #   print(prod)
    return render(request, 'hello.html', {'name': 'Reza', 'products': list(queryset1), 'products2': list(queryset2), 'products3': list(queryset3)})


def tem_func(request):
    queryset1 = Collection.objects.filter(featured_product_id__isnull=True)
    queryset2 = Customer.objects.filter(email__icontains='.com')
    queryset3 = Order.objects.filter(customer_id=1)
    queryset4 = OrderItem.objects.filter(product__collection_id=3)
    queryset5 = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').all().order_by('-placed_at')[:5]
    return render(request, 'temp2.html', {'collection_info': list(queryset1), 'customer_info': list(queryset2), 'order_info': list(queryset3), 'orderitem_info': list(queryset4), 'ord_info': list(queryset5)})
