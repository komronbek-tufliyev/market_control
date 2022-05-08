from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='category')
    farm_name = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True) 
    experied_date = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Business(models.Model):
    name = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='business/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



