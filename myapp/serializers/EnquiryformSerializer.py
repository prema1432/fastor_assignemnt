from rest_framework.serializers import ModelSerializer

from myapp.models.Enquiryform import Enquiryform
from user.models import CustomUser
from user.serializers.UserSerializer import UserSerializers

class AdminEnquiryformModelSerializers(ModelSerializer):
    student = UserSerializers()

    class Meta:
        model = Enquiryform
        fields = ('id', 'student', 'department', 'course','semester','employee')
        # depth = 1

class EmpClaimEnquiryformModelSerializers(ModelSerializer):
    # student = UserSerializers()

    class Meta:
        model = Enquiryform
        fields = ('id', 'employee')
        # depth = 1

class EnquiryformModelSerializers(ModelSerializer):
    student = UserSerializers()

    class Meta:
        model = Enquiryform
        fields = ('id', 'student', 'department', 'course','semester')
        # depth = 1

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('student')
        user = CustomUser.objects.create(
            name=user_data['name'],
            email=user_data['email'],
            phone_number=user_data['phone_number'],is_student=True)
        user.set_password(user_data['password'])
        user.save()
        emp = Enquiryform.objects.create(
            student=user,
            department=validated_data['department'],
            course=validated_data['course'],
            semester=validated_data['semester']
        )
        return emp

