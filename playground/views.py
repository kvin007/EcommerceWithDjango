from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from store.models import CartItem, Product, Customer, Collection, Order, OrderItem, Cart, CartItem
from tags.models import Tag, TaggedItem


def say_hello(request):
    # None
    # queryset = Customer.objects.filter(email__icontains='.com')
    # queryset = Collection.objects.filter(featured_product__is_null=True)
    # queryset = Product.objects.filter(customer__id=1)
    # queryset = Product.objects.filter(product__collection__id=3)

    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # queryset = Product.objects.order_by('unit_price','-title').reverse()

    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.latest('unit_price')

    # products = Product.objects.all()[5:10]

    # products = Product.objects.values('id','title','collection__title')
    # products = Product.objects.values_list('id','title','collection__title')

    # queryset =  Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    # queryset = Product.objects.only('id','title') #BE CAREFUl because if not may have thousands of queries
    # queryset = Product.objects.defer('description')  #ALL BUT DESCRIPTION. AND BE CAREFUL AGAIN

    # select_related (1)
    # prefetch_related (n)

    # queryset = Product.objects.prefetch_related('collection').all()

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # result = Product.objects.filter(collection__id=1).aggregate(count = Count('id'), min_price = Min('unit_price'))

    # queryset = Customer.objects.annotate(
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    # )

    # queryset = Customer.objects.annotate(
    #     orders_count = Count('order') #Can not be order_set
    # )

    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field= DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price = discounted_price
    # )

    # queryset = Customer.objects.annotate(last_order_id=Max("order__id"))
    # queryset = Collection.objects.annotate(product_count=Count("product"))
    # queryset = Customer.objects.annotate(orders_count= Count('order')).filter(orders_count__gt=5)

    # queryset = Customer.objects.annotate(
    #     amount_spent=Sum(
    #         F("order__orderitem__unit_price") * F("order__orderitem__quantity")
    #     )
    # )

    # queryset = Product.objects.annotate(total_sales = Count('orderitem__order__id')).order_by('-total_sales')[:5]

    # queryset = TaggedItem.objects.get_tags_for(Product,1)
    
    # cart = Cart()
    # cart.save()
    # cart_item = CartItem()
    # cart_item.cart = cart
    # cart_item.product = Product(pk=1)
    # cart_item.quantity = 1
    # cart_item.save()

    return render(request, "hello.html", {"name": "Mosh"})
    # return render(request, "hello.html", {"name": "Mosh", "orders": list(queryset)})
