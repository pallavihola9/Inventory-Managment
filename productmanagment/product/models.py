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
         """
        Update product information.

        Args:
            name (str): New name of the product.
            description (str): New description of the product.
            price (float): New price of the product.
        """
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
        """
        Add a product to the inventory.

        Args:
            product (Product): Product object to be added to the inventory.
        """
        self.products.add(product)
    
    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (str): ID of the product to be removed.
        """
        product = Product.objects.filter(product_id=product_id).first()
        if product:
            self.products.remove(product)
            product.delete()
    
    def update_stock(self, product_id, quantity):
        """
        Update the stock quantity of a product.

        Args:
            product_id (str): ID of the product to update stock.
            quantity (int): Quantity to increase or decrease in the stock.
        """
        product = Product.objects.filter(product_id=product_id).first()
        if product:
            product.quantity += quantity
            if product.quantity < 0:
                product.quantity = 0
            product.save()
    
    def process_sale(self, product_id, quantity):
        """
        Process a sale by reducing the stock quantity of the sold products.

        Args:
            product_id (str): ID of the product to be sold.
            quantity (int): Quantity of the product to be sold.

        Returns:
            float: Total cost of the sale.
        """
        product = Product.objects.filter(product_id=product_id).first()
        if product and product.quantity >= quantity:
            product.quantity -= quantity
            product.save()
            return product.price * quantity
        else:
            raise ValueError("Not enough stock for this sale")

    def generate_report(self):
         """
        Generate a report of all products with their current stock levels and prices.

        Returns:
            QuerySet: Queryset containing all products in the inventory.
        """
        return self.products.all()

    def generate_low_stock_report(self, threshold=5):
        """
        Generate a low-stock report listing all products with stock below the threshold.

        Args:
            threshold (int): Minimum stock quantity for a product to be considered low stock.

        Returns:
            QuerySet: Queryset containing products with stock below the threshold.
        """
        return self.products.filter(quantity__lt=threshold)
