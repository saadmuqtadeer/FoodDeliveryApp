from django.contrib import admin
from pricing.models import Organization, Item, Pricing
# Register your models here.
admin.site.register(Organization)
admin.site.register(Item)
admin.site.register(Pricing)