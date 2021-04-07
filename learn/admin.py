from django.contrib import admin
from learn.models import Course, Category, Cart, OrderedCourse

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(OrderedCourse)

