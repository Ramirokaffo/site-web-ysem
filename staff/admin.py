from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    date_hierarchy = "born_date"
    list_display = ("user", "gender", "born_date", "phone")
    autocomplete_fields = ["user"]


admin.site.register(Staff, StaffAdmin)

# Register your models here.
