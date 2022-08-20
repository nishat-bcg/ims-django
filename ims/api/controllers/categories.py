from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.status import HTTP_200_OK

from api.models.category import Category
from api.serializers.categories import CategorySerializer

class CategoryController(APIView):
    def get(self, request):
        qs = Category.objects.all()
        serializer = CategorySerializer(qs, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK) 