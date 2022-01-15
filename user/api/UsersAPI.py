from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import CustomUser
from user.serializers.UserSerializer import UserSerializers


class AllUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if self.request.user.is_superuser == True:
            allusers = CustomUser.objects.all()
            serializer = UserSerializers(allusers, many=True)
            return Response(serializer.data)
        else:
            return Response({"status": "failed", "message": "superuser only access this api "},
                            status=status.HTTP_200_OK)
