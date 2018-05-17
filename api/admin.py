from django.contrib import admin

# Register your models here.
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
  pass
