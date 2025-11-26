from rest_framework import serializers
from .models import Telephone

class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = '__all__'