from django.contrib import admin
from .models import TA_User, TAProfile, AvailabilitySlot

class AvailabilitySlotInline(admin.TabularInline):
    model = AvailabilitySlot
    extra = 1
    can_delete = True

@admin.register(TAProfile)
class TAProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "description")
    inlines = [AvailabilitySlotInline]

@admin.register(TA_User)
class TAUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "is_ta")
