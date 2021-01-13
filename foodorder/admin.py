from django.contrib import admin
from  .models import OurSpeciality
from .models import TodaySpecial
from .models import Product
from .models import Category
from .models import Orders

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
# Register your models here.
admin.site.register(OurSpeciality)
admin.site.register(TodaySpecial)
admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(Orders)


