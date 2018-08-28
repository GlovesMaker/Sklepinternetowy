from decimal import Decimal
from django.conf import settings
from apka.models import Product
from coupons.models import Coupon
from orders.models import Order

class Cart(object):
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')
        
    def add(self, product, quantity=1, update_quantity=False):

        product_id = str(product.id)
        #if product.stock >= quantity:
        if not product_id in self.cart:
            self.cart[product_id] = self.cart.get(product_id, {'quantity': quantity, 'price': str(product.price)})
        else:
          self.cart[product_id]['quantity'] += quantity
        self.save()
            
       
            
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        del self.cart[product_id]
        self.save()
        

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
            
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    #first_name
    @property

    def coupon(self):
        check_cod = Order.objects.all()
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None
            #for x in check_cod:
                #lista.append(x.first_name)
                #if lista[:] != str('xxxw'):
                    #return Coupon.objects.get(id=self.coupon_id)        
                #else:
                    #return None    

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) \
                * self.get_total_price()
        return Decimal('0')
    
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def total_send(self):
        return 20 + self.get_total_price() - self.get_discount()       

