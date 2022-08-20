from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from api.models.customer import Customer
from api.serializers.customer import CustomerSerializer

class CustomersController(APIView):

    def get(self, request):
        qs = Customer.objects.all()
        serializer = CustomerSerializer(qs, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK) 

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data = serializer.errors, status=HTTP_400_BAD_REQUEST)

class CustomerController(APIView):

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        qs = self.get_object(pk)
        serializer = CustomerSerializer(qs)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        qs = self.get_object(pk=pk)
        serializer = CustomerSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = self.get_object(pk=pk)
        qs.delete()
        return Response(status=HTTP_204_NO_CONTENT)