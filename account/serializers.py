from rest_framework import serializers

from .models import Acccount, Address

class AcccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acccount
        fields = '__all__'
        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
    def validate(self, data):
        if 'country' in data and 'postalcode' in data:
            if data['country'] == 'USA' and len(data['postalcode']) != 5:
                raise serializers.ValidationError("Postalcode should be 5 digits")
        return data