from sqlite3 import IntegrityError
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from api.models.productOrder import ProductOrder
from api.serializers.productOrders import ProductOrderSerializer
from api.models.product import Product
from api.serializers.productOrders import ProductOrderSerializer

class ProductOrdersController(APIView):

    def get_product(self, request):
        try:
            return Product.objects.filter(id=request.data["product"]).first()
        except Product.DoesNotExist:
            raise Http404

    def get(self, request):
        qs = ProductOrder.objects.all()
        serializer = ProductOrderSerializer(qs, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK) 

    def post(self, request):
        serializer = ProductOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data = serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProductOrderController(APIView):

    def get_object(self, pk):
        try:
            return ProductOrder.objects.get(pk=pk)
        except ProductOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        qs = self.get_object(pk)
        serializer = ProductOrderSerializer(qs)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        qs = self.get_object(pk=pk)
        serializer = ProductOrderSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = self.get_object(pk=pk)
        qs.delete()
        return Response(status=HTTP_204_NO_CONTENT)
