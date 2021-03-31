from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    url = models.SlugField()
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'uploaded')
    price = models.IntegerField()
    about =models.TextField()
    stock = models.BooleanField(default = True)
    slug =models.SlugField()
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class addtocart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

class cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(addtocart)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
