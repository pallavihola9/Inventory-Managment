from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def update_info(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price is not None:
            self.price = price
        self.save()
    
    def __str__(self):
        return f"{self.name} ({self.product_id})"

class Inventory(models.Model):
    products = models.ManyToManyField(Product)

    def add_product(self, product):
        self.products.add(product)
    
    def remove_product(self, product_id):
        product = Product.objects.filter(product_id=product_id).first()
        if product:
            self.products.remove(product)
            product.delete()
    
    def update_stock(self, product_id, quantity):
        product = Product.objects.filter(product_id=product_id).first()
        if product:
            product.quantity += quantity
            if product.quantity < 0:
                product.quantity = 0
            product.save()
    
    def process_sale(self, product_id, quantity):
        product = Product.objects.filter(product_id=product_id).first()
        if product and product.quantity >= quantity:
            product.quantity -= quantity
            product.save()
            return product.price * quantity
        else:
            raise ValueError("Not enough stock for this sale")

    def generate_report(self):
        return self.products.all()

    def generate_low_stock_report(self, threshold=5):
        return self.products.filter(quantity__lt=threshold)
