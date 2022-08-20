from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.status import HTTP_200_OK

from api.models.customerGroup import CustomerGroup
from api.serializers.customerGroups import CustomerGroupSerializer

class CustomerGroupController(APIView):
    def get(self, request):
        qs = CustomerGroup.objects.all()
        serializer = CustomerGroupSerializer(qs, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK) 