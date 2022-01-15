from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models.Employee import Employee
from myapp.serializers.EmployeeSerializer import EmployeeModelSerializers


class AllEmployees(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if self.request.user.is_superuser == True:
            emp = Employee.objects.all()
            serializer = EmployeeModelSerializers(emp, many=True)
            return Response(serializer.data)
        else:
            return Response({"status": "failed", "message": "superuser only access this api "},
                            status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EmployeeModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)