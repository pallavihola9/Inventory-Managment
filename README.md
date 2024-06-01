# Inventory Management System

This project provides an inventory management system implemented using Django.

## Setup

1. Clone the repository:
git clone <https://github.com/pallavihola9/Inventory-Managment>
2. Install dependencies:
 pip install django
 pip install djangorestframework
3. Apply migrations: python manage.py makemigrations , python manage.py migrate
4. Run the development server: python manage.py runserver
5. 
## Usage

1. Add Product:
- Endpoint: `/add_product/`
- Method: `POST`
- Body: JSON data including product details (product_id, name, description, price, quantity).

2. Update Product:
- Endpoint: `/update_product/<product_id>/`
- Method: `POST`
- Body: JSON data with updated product information.

3. Remove Product:
- Endpoint: `/remove_product/<product_id>/`
- Method: `POST`

4. Update Stock:
- Endpoint: `/update_stock/<product_id>/`
- Method: `POST`
- Body: JSON data with quantity to increase or decrease stock.

5. Process Sale:
- Endpoint: `/process_sale/<product_id>/`
- Method: `POST`
- Body: JSON data with quantity of product sold.

6. Generate Report:
- Endpoint: `/report/`
- Method: `GET`

7. Generate Low Stock Report:
- Endpoint: `/low_stock_report/`
- Method: `GET`
- Params: `threshold` (optional) - Minimum stock quantity for low stock products.


