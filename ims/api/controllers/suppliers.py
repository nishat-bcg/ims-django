from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.status import HTTP_200_OK

from api.models.supplier import Supplier
from api.serializers.suppliers import SupplierSerializer

class SupplierController(APIView):
    def get(self, request):
        qs = Supplier.objects.all()
        serializer = SupplierSerializer(qs, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK) 