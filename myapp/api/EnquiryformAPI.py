from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from myapp.models.Enquiryform import Enquiryform
from myapp.serializers.EnquiryformSerializer import EnquiryformModelSerializers, EmpClaimEnquiryformModelSerializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.serializers.EmployeeSerializer import EmployeeModelSerializers


class AllEnquiryforms(APIView):

    def get(self, request, format=None):
        enq_form = Enquiryform.objects.filter(employee=None)
        serializer = EnquiryformModelSerializers(enq_form, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = EnquiryformModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeClaim(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Enquiryform.objects.get(pk=pk)
        except Enquiryform.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        if self.request.user.is_employee == True:
            snippet = self.get_object(pk)
            serializer = EmpClaimEnquiryformModelSerializers(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save(employee_id=self.request.user.id)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "failed", "message": "employees only claim this forms "},
                            status=status.HTTP_200_OK)