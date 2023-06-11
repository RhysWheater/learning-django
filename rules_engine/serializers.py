from rest_framework import serializers
from .models import *

class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'
