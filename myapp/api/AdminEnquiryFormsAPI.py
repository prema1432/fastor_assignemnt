from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models.Enquiryform import Enquiryform
from myapp.serializers.EnquiryformSerializer import AdminEnquiryformModelSerializers


class AdminEnquiryforms(APIView):
    permission_classes = [IsAuthenticated]
    #
    # def get_parsers(self):
    #     if self.request.user.is_superuser == True:
    #         return Enquiryform.objects.all()
    #     elif self.request.user.is_employee == True:
    #         return Enquiryform.objects.filter(employee_id=self.request.user.id)
    #     else:
    #         return None

    def get(self, request, format=None):
        if self.request.user.is_superuser == True:
            enq_form = Enquiryform.objects.all()
        elif self.request.user.is_employee == True:
            enq_form = Enquiryform.objects.filter(employee_id=self.request.user.id)
        else:
            enq_form = None


        # enq_form = self.get_queryset()
        serializer = AdminEnquiryformModelSerializers(enq_form, many=True)
        return Response(serializer.data)
