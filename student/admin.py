from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ["user", "matricule"]
    date_hierarchy = "born_date"
    list_display = ("matricule", "user", "gender", "born_date", "phone")
    autocomplete_fields = ["user"]


admin.site.register(Student, StudentAdmin)
