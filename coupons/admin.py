from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'Valid_to', 'discount']
    list_filter = ['active', 'valid_from', 'Valid_to']
    search_fields = ['code']
admin.site.register(Coupon, CouponAdmin)
