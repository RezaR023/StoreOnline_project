from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, ExpressionWrapper, DecimalField, Value, DateTimeField, DateField
from django.db.models.aggregates import Avg, Count, Max, Min, Sum, StdDev, Variance
from store.models import Product, Customer, Collection, Order, OrderItem
# Create your views here.


def say_hello2(request):
    # To set update add pk=11 in the arument
    collection = Collection(pk=11)
    collection.title = 'Games'
    collection.featured_product = Product(pk=2)
    collection.save()
    collection.id

    return render(request, 'sh.html')


def say_hello(request):
    result = Product.objects.aggregate(
        count=Count('id'), min_price=Max('unit_price')-Min('unit_price'))
    queryset1 = Product.objects.filter(unit_price__range=(10, 30))
    queryset2 = Product.objects.filter(
        ~Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    # queryset33 and queryset3 have the same results.
    queryset3 = Product.objects.filter(
        id=F('orderitem__product_id')).distinct().order_by('title')
    queryset33 = Product.objects.filter(id__in=OrderItem.objects.values(
        'product_id').distinct()).order_by('title')

    diction = {'name': 'Reza', 'products': list(queryset1), 'products2': list(
        queryset2), 'products3': list(queryset3), 'res1': result}
    return render(request, 'hello.html', diction)


def tem_func(request):
    res2 = Order.objects.aggregate(The_number_of_oders=Count(id))
    queryset0 = OrderItem.objects.filter(
        product_id=1).filter(order__payment_status='C')
    res3 = OrderItem.objects.filter(product_id=1).filter(
        order__payment_status='C').aggregate(The_number_of_Soledproduct1=Sum('quantity'))
    res4 = Order.objects.filter(customer_id=1).aggregate(
        the_orders_of_cust1=Count('id'))
    res5 = Product.objects.filter(collection_id=3).aggregate(min_is=Min(
        'unit_price'), max_is=Max('unit_price'), ave_is=Avg('unit_price'))
    queryset1 = Collection.objects.filter(featured_product_id__isnull=True)
    queryset2 = Customer.objects.filter(email__icontains='.com')
    queryset3 = Order.objects.filter(customer_id=1)
    queryset4 = OrderItem.objects.filter(product__collection_id=3)
    queryset5 = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').all().order_by('-placed_at')[:5]

    queryset6 = Customer.objects.annotate(orders_count=Count('order'))
    queryset7 = Product.objects.annotate(
        discouned_price=ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField()))
    queryset8 = Customer.objects.annotate(last_order_id=Max('order__id'))
    queryset9 = Collection.objects.annotate(
        NUmber_of_products=Count('product__id'))
    queryset10 = Customer.objects.annotate(
        cus_with_more5_orders=Count('order__id')).filter(cus_with_more5_orders__gt=5)
    queryset11 = Customer.objects.annotate(
        money_spend=Sum(F('order__orderitem__unit_price')*F('order__orderitem__quantity')))
    queryset12 = Product.objects.annotate(
        soled_prod=Sum(F('orderitem__unit_price')*F('orderitem__quantity'))).order_by('-soled_prod')[:5]

    dic2 = {'collection_info': list(queryset1), 'customer_info': list(queryset2), 'order_info': list(
        queryset3), 'orderitem_info': list(queryset4), 'ord_info': list(queryset5),
        'qs6': list(queryset6), 'qs7': list(queryset7), 'qs80': list(queryset8), 'qs12': list(queryset12),
        'qs0': list(queryset0), 'res2': res2, 'res3': res3, 'res4': res4, 'res5': res5}
    dic2t = {'qs80': list(queryset8)}
    return render(request, 'temp2.html', dic2)
