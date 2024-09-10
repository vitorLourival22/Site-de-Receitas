from django.contrib import admin
from .models import Food
# Register your models here.

@admin.register(Food)
class KitchenAdmin(admin.ModelAdmin):
     list_display = ('name','description','Category','date_publication',)
     list_filter = ('Category',)


