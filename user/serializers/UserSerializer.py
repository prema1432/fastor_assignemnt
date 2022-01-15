from rest_framework import serializers

from user.models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        # exclude = ('password',)
