from django.contrib import admin
from .models import Servicemod
from .models import Usermod
from .models import Ordermod



@admin.register(Servicemod)
class AdminService(admin.ModelAdmin):
    list_display = ["name", "price", "count"]


@admin.register(Usermod)
class AdminService(admin.ModelAdmin):
    list_display = ["user", "mobile_phone", "name_org", "address_org"]

@admin.register(Ordermod)
class AdminService(admin.ModelAdmin):
    list_display = ["servicemod", "usermod", "date_order", "executed_order"]


