from rest_framework import serializers

from .models import ListOfUser

class ListOfUserSerializer(serializers.ModelSerializer): #ATTENTION ICI C'EST BIEN MODELSERIALIZER
    class Meta:
        model = ListOfUser
        fields = ('__all__')
