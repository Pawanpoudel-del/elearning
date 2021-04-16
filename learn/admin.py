from django.contrib import admin
from learn.models import Course, Category, Cart, OrderedCourse, Address, Contact

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(OrderedCourse)
admin.site.register(Contact)

