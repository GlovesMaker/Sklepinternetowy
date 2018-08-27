from django.contrib import admin
from .models import Order, OrderItem
import csv
import datetime
from django.http import HttpResponse

    
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachent ; \
        filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
            data_row = []
            for field in fields:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                data_row.append(value)
            writer.writerow(data_row)
    return response
export_to_csv.short_description = 'eksport do CSV'


    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['order']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'coupon', 'created', 'updated','model_wysylki','paczkomat','nr_telefonu','Kurier_InPost','Paczkomaty_InPost','Poczta_Polska']
    list_filter = ['paid', 'created', 'updated', 'coupon']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)
