from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers.CustomLoginSerializer import CustomLoginSerializer


class CustomLoginAPI(TokenObtainPairView):
    serializer_class = CustomLoginSerializer
    print(serializer_class.data)
