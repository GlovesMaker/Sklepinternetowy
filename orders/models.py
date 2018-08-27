from django.db import models
from apka.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon

wysylka = (
        ('1', 'Kurier InPost  - pobranie'),
        ('2', 'Paczkomaty InPost - pobranie'),
        ('3', 'Poczta Polska - pobranie'),)



class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Imię')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Nazwisko*')
    email = models.EmailField(verbose_name='E-mail')
    address = models.CharField(max_length=250,blank=True, verbose_name='Adres*')
    postal_code = models.CharField(max_length=20,blank=True, verbose_name='Kod pocztowy*')
    city = models.CharField(max_length=100,blank=True, verbose_name='Miasto*')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, related_name='orders',
                               null=True,
                               blank=True)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    model_wysylki = models.BooleanField(default=False)
    paczkomat = models.CharField(max_length=250, blank=True, verbose_name='Kod paczkomatu*')
    nr_telefonu = models.CharField(max_length=11, verbose_name='Nr telefonu')
    uwaga = models.CharField(max_length=250, blank=True, verbose_name='Uwagi dla nadawcy*')
    Kurier_InPost = models.BooleanField(default=False, verbose_name='Kurier InPost  - pobranie')
    Paczkomaty_InPost = models.BooleanField(default=False, verbose_name='Paczkomaty InPost - pobranie (podaj nazwa paczkomatu)')
    Poczta_Polska = models.BooleanField(default=False, verbose_name='Poczta Polska - pobranie')
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / decimal('100')) 
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

        
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
