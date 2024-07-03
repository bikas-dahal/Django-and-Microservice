from rest_framework import serializers

from .models import Acccount 

class AcccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acccount
        fields = '__all__'