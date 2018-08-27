from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from projekt.utils import render_to_pdf #created in step 4
from django.http import HttpResponse
from orders.models import OrderItem
from orders.models import Order
from cart.cart import Cart

#r =[77,78,79,80]


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        template = get_template('invoice.html')
        p = Order.objects.all()
        #asd = OrderItem.objects.get(id=r[2])
        

        for x in p:
          
            
            #asd.order - id dla zamowienia
           
            context = {#'id_test':asd.order,
                       #'id_atest':asd.id,
                       #'id_atest':asd.product,
                       #'id_btest':asd.price,
                       #'id_ctest':asd.quantity,
                       'id': x.id,
                       'first_name': x.first_name,
                       'last_name': x.last_name,
                       'email': x.email,
                       #'address': x.address,
                       #'postal_code': x.postal_code,
                       #'city': x.city,
                       'created': x.created,
                       'coupon': x.coupon,
                       'discount': x.discount,
                       #'model_wysylki': x.model_wysylki,
                       #'nr_telefonu': x.nr_telefonu,
                       'paczkomat': x.paczkomat,
                       'uwaga': x.uwaga,
                       }
            
            html = template.render(context)
            pdf = render_to_pdf('invoice.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content ="inline; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                download = request.GET.get("download")
                if download:
                    content ="attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Nie znaleziono")
