from django.db import models

# many-to-many realtionship between promotion and product


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    feature_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    # To create your primery key
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    colletions = models.ForeignKey(Collection, on_delete=models.PROTECT)
    # If you want Django use a specific name (here is products) in promotion class, use option related_name
    # promotions = models.ManyToManyField(Promotion,related_name='products')
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'SILVER'),
        (MEMBERSHIP_GOLD, 'GOLD'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255, default='-')
    # for one to one relationship
    # customer = models.OneToOneField(
    #   Customer, on_delete=models.CASCADE, primary_key=True)

    # for one to many relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):
    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILD_STATUS = 'F'

    PAYMENT_STATUS = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Complete'),
        (FAILD_STATUS, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    paymant_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default=PENDING_STATUS)

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

# Shopping cart


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class cartItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
