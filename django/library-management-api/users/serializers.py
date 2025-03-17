from django.contrib.auth.models import User,Group
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=['id','username','email','password','password','first_name','last_name']
    extra_kwargs={'password':{'write_only': True}}
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    group,created = Group.objects.get_or_create(name='Member')
    user.groups.add(group)
    user.save()
    return user
