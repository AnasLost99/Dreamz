from django.contrib import admin
from .models import Product,Category,Profile,Reviews,Cart,CartItem
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(CartItem)


