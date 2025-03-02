from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

""" class UserCreateSerializer(BaseUserSerializer):
  class meta(BaseUserSerializer.Meta):
    fields = ['id', 'email', 'password', 'first_name', 'last_name','address','phone_number'] """
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'first_name',
                  'last_name', 'address', 'phone_number']