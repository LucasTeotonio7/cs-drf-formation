from django.contrib import admin
from apps.customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','cpf', 'rg', 'phone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 25

admin.site.register(Customer, CustomerAdmin)
