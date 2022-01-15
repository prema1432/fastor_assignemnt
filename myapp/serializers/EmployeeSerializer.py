from rest_framework.serializers import ModelSerializer

from myapp.models.Employee import Employee
from user.models import CustomUser
from user.serializers.UserSerializer import UserSerializers


class EmployeeModelSerializers(ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Employee
        fields = ('id', 'user', 'department', 'year_of_exp')
        # depth = 1

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(
            name=user_data['name'],
            email=user_data['email'],
            phone_number=user_data['phone_number'],is_employee=True)
        user.set_password(user_data['password'])
        user.save()
        emp = Employee.objects.create(
            user=user,
            department=validated_data['department'],
            year_of_exp=validated_data['year_of_exp']
        )
        return emp

