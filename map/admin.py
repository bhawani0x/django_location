from django.contrib import admin
from .models import BaseAddress
from .forms import AddressAdminForm

@admin.register(BaseAddress)
class BaseAddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = ['address', 'location']
