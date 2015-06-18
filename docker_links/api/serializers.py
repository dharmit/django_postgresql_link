from rest_framework.serializers import ModelSerializer
from api.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        fields = ('id', 'name',)
        model = User
