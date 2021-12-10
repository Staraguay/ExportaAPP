from django.db import models

# Create your models here.

class Buyer(models.Model):

    buyer_id = models.IntegerField(primary_key=True, null=False, blank=False, verbose_name='BuyerID')
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name='Name')
    location = models.CharField(null=False, blank=False, max_length=100, verbose_name='Location')
    registration_date = models.DateTimeField(null=False, blank=False, max_length=100, verbose_name='RegistrationDate')
    industry = models.CharField(null=False, blank=False, max_length=100, verbose_name='Industry')
    membership = models.CharField(null=False, blank=False, max_length=100, verbose_name='Membership')
    active = models.BooleanField(null=False, blank=False, max_length=100, verbose_name='Active')

    class Meta:

        db_table = 'Buyer'
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'
        ordering = ['buyer_id']

class Order(models.Model):

    order_id = models.IntegerField(primary_key=True,null=False, blank=False, verbose_name='OrderID')
    product_description = models.TextField(null=False, blank=False, verbose_name='PDescription')
    target_price = models.IntegerField(null=False, blank=False, verbose_name='Price')
    quantity = models.IntegerField(null=False, blank=False, verbose_name='Quantity')
    lead_time = models.DateTimeField(null=False, blank=False, verbose_name='LeadTime')
    recurrence_purchase = models.CharField( max_length=100, null=False, blank=False, verbose_name='Recurrence')
    tech_pack = models.CharField(max_length=100, null=False, blank=False, verbose_name='Tech')
    comments = models.TextField(null=False, blank=False, verbose_name='Comments')
    buyerId = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    class Meta:

        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['order_id']


