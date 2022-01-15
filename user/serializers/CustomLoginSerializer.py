from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomLoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CustomLoginSerializer, self).validate(attrs)

        data.update({'name': self.user.name})
        data.update({'email': self.user.email})
        data.update({'mobile_number': self.user.phone_number})
        data.update({'is_superuser': self.user.is_superuser})
        data.update({'is_employee': self.user.is_employee})
        data.update({'is_student': self.user.is_student})
        data.update({'is_active': self.user.is_active})
        data.update({'id': self.user.id})
        return data
