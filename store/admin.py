from typing import Any, List, Optional, Tuple
from django.contrib import admin, messages
# from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.html import format_html, urlencode
# from django.utils.http import urlencode
from django.urls import reverse
from . import models
# from tags.models import TaggedItem
from django.db.models.aggregates import Avg, Count, Max, Min, Sum, StdDev, Variance

# Register your models here.


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'ínventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>90', 'High')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        if self.value() == '>90':
            return queryset.filter(inventory__gt=90)


# class TagInline(GenericTabularInline):
#     autocomplete_fields = ['tag']
#     model = TaggedItem


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    actions = ['clear_inventory']
    autocomplete_fields = ['collection']
    # inlines = [TagInline]
    list_display = ['title', 'unit_price',
                    'inventory_status', 'COLLECTION_TITLE']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_editable = ['unit_price']
    list_per_page = 20
    search_fields = ['title']

    # list_select_related = ['collection']

    def COLLECTION_TITLE(self, product):
        return product.collection.title

    # To implement sorting based on inventory_status, use admin.display decorator

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.SUCCESS
        )


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection__id': str(collection.id)
               }))
        return format_html('<a href="{}">{}</a>', url,  collection.products_count)
        # return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))

# admin.site.register(models.Product)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20
    search_fields = ['first_name', 'last_name']

    # list_select_related = ['order']

    @admin.display(ordering='orders_count')
    def orders_count(self, cuss):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(cuss.id)
            })
        )
        return format_html('<a href="{}"> {} </a>', url, cuss.orders_count)
        # return cuss.orders_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count('order__id'))


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    # min_num = 1
    # max_num = 11


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'payment_status', 'customer']
    list_editable = ['payment_status']
    list_per_page = 10
    list_select_related = ['customer']

    # def customer_list(self, order):
    #   return order.customer.first_name, ' ', order.customer.last_name


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'unit_price']
    list_editable = ['quantity', 'unit_price']
