from django.contrib import admin
from learn.models import Course, Category, addtocart, cart 

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(addtocart)
admin.site.register(cart)
