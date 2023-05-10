from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            'name',
            "password",
            "password2",
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password2(self, value):
        password1 = self.get_initial().get('password')
        
        # Check if two passwords are equal
        if password1 and password1 != value:
            raise serializers.ValidationError("Passwords mismatched")
        
        return value
    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('email'),
            name=self.validated_data.get('name'),
            password=validated_data.get('password'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        
        return user
    

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    
