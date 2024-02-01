from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    def _str_(self):
        return self.name 

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=10)
    details=models.TextField()
    image=models.ImageField(upload_to='profile_pic',null=True,blank=True)
    offer=models.CharField(max_length=30)
    ratings=models.CharField(max_length=10)
    originalprice=models.CharField(max_length=10)
    ctry=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def _str_(self):
        return self.name 
    
class Profile(models.Model):
    
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to='profile_pic',null=True,blank=True)
    email=models.CharField(max_length=30)
    


    def _str_(self):
        return str(self.user)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.CharField(max_length=1130)
    post=models.ForeignKey(Product,on_delete=models.CASCADE)


    def _str_(self):
        return str(self.user)
    
class Cart(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    
    # @property
    # def total_price(self):
    #     cartitems = self.cartitems.all()
    #     quantity = sum({item.quantity for item in cartitems})
    #     return quantity
    
    # @property
    # def num_of_items(self):
    #     cartitems = self.cartitems.all()
    #     total = sum({item.price for item in cartitems})
    #     return total

    
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='items')
    cart=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='cartitems')
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
    
    # @property
    # def price(self):
    #     total_price = self.product.price * self.quantity
    #     return total_price

    
