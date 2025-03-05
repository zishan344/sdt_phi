from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

""" class UserCreateSerializer(BaseUserSerializer):
  class meta(BaseUserSerializer.Meta):
    fields = ['id', 'email', 'password', 'first_name', 'last_name','address','phone_number'] """
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'first_name',
                    'last_name', 'address', 'phone_number']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = ['id', 'email', 'first_name',
                    'last_name', 'address', 'phone_number']