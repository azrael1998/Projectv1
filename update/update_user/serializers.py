from rest_framework import serializers
from .models import RegisterUserAppuser

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char))+s)
    return result

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUserAppuser
        fields = ['name','email','password']
        # extra_kwargs={'password': {'write_only': True}}
    


    def create(self,validated_data):
        user = RegisterUserAppuser.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            password = encrypt(validated_data['password'],4),

        )
        return user