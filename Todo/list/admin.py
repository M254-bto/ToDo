from django.contrib import admin
from. import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ("date_added", "text")


admin.site.register(models.ToDo)