from rest_framework import serializers
from .models import ImZacadQ1Bk, ImZacadQ2Bk

class Q1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ImZacadQ1Bk
        fields = '__all__'

class Q2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ImZacadQ2Bk
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImZacadQ1Bk
        exclude = 'ZQ_PK, ZQ_CODE'