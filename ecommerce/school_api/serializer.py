from dataclasses import fields
from pyexpat import model
from .models import Student
from rest_framework import serializers

class Student_serializer(serializers.ModelSerializer):
    class meta:
        model = Student
        fields = '__all__'