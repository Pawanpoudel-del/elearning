from django.db import models
from django.conf import settings
PAYMENT_METHOD = [
    ('COD','CASH ON DELIVERY'),
    ('ONLINE','KHALTI PAYMENT')
]

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
    detail =models.TextField()
    stock = models.BooleanField(default = True)
    slug =models.SlugField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

class Address(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pradesh=models.IntegerField()
    city=models.TextField()
    country=models.TextField()
    contact_number=models.IntegerField()

    def __str__(self):
        return self.user.username

class OrderedCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ManyToManyField(Cart)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    sum = models.IntegerField()
    payment_choices = models.CharField(max_length =200, choices = PAYMENT_METHOD)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name= models. CharField(max_length=200) 
    email = models.EmailField()
    message= models.TextField()

    def __str__(self):
        return self.name
        