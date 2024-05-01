from django.contrib import admin
from .models import Vendor, PurchaseOrder, Performance

# Register your models here.
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(Performance)