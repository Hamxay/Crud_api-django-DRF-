from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100)
    # age = serializers.IntegerField()
    # location = serializers.CharField(max_length=1000)
    class Meta:
        model = Student
        fields = '__all__'

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
