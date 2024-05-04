from django.contrib import admin
from deals.models import Category, Deal, Alert

admin.site.register(Category)
admin.site.register(Deal)
admin.site.register(Alert)