from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product, Inventory
from .serializers import ProductSerializer

class AddProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            inventory = Inventory.objects.first()  # Assuming single inventory for simplicity
            product = serializer.save()
            inventory.products.add(product)  # Associate the product with the inventory
            return Response({'message': 'Product added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProductView(APIView):
    def post(self, request, product_id):
        product = get_object_or_404(Product, product_id=product_id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            inventory = Inventory.objects.first()  # Assuming single inventory for simplicity
            product = serializer.save()
            inventory.products.add(product)  # Associate the product with the inventory
            return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveProductView(APIView):
    def post(self, request, product_id):
        inventory = Inventory.objects.first()  # Assuming single inventory for simplicity
        inventory.remove_product(product_id)
        return Response({'message': 'Product removed successfully'}, status=status.HTTP_200_OK)

class UpdateStockView(APIView):
    def post(self, request, product_id):
        inventory = Inventory.objects.first()  # Assuming single inventory for simplicity
        quantity = int(request.data['quantity'])
        inventory.update_stock(product_id, quantity)
        return Response({'message': 'Stock updated successfully'}, status=status.HTTP_200_OK)

class ProcessSaleView(APIView):
    def post(self, request, product_id):
        inventory = Inventory.objects.first()  # Assuming single inventory for simplicity
        quantity = int(request.data['quantity'])
        try:
            total_cost = inventory.process_sale(product_id, quantity)
            return Response({'message': 'Sale processed successfully', 'total_cost': total_cost}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ReportView(APIView):
    def get(self, request):
        inventory = Inventory.objects.first()
        print("Inventory:", inventory)  # Debugging
        if not inventory:
            return Response({'error': 'Inventory not found'}, status=status.HTTP_404_NOT_FOUND)

        products = inventory.generate_report()
        print("Products:", products)  # Debugging
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LowStockReportView(APIView):
    def get(self, request):
        inventory = Inventory.objects.first()  # Assuming single inventory for simplicity
        threshold = int(request.query_params.get('threshold', 5))
        products = inventory.generate_low_stock_report(threshold)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
