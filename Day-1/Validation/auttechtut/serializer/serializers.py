from rest_framework import serializers
from .models import comment, Student

class CommentSerializer(serializers.Serializer):    
    email = serializers.EmailField(error_messages = {"required":"Email is required"})
    name = serializers.CharField(error_messages = {"required":"Name is required"})
    date = serializers.DateField()

    def create(self, validated_data):
        return comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return comment.save(instance, validated_data)

class StudentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField(error_messages = {"required":"rollno is required"})
    name = serializers.CharField(error_messages = {"required":"name is required"})
    department = serializers.CharField(error_messages = {"required":"department is required"})
    address = serializers.CharField(error_messages = {"required":"address is required"})

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return Student.save(instance, validated_data)



