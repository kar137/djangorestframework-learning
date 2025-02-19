from rest_framework import serializers
from .models import comment, Student


class StudentSerializer(serializers.Serializer):
    title = serializers.CharField(error_messages = {"required":"title is required"}, required= True)
    roll_no = serializers.IntegerField(error_messages = {"required":"rollno is required"})
    name = serializers.CharField(error_messages = {"required":"name is required"})
    department = serializers.CharField(error_messages = {"required":"department is required"})
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    address = serializers.CharField(error_messages = {"required":"address is required"})

    # # field level validation check for title

    # def validate_title(self, value):
    # # checks table title is about student or not
    #     if value.lower() != 'student':
    #         raise serializers.ValidationError("title must contain student")
    #     return value
    
    # object level validation

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("start date should be before finish date")
        return data


    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return Student.save(instance, validated_data)
    
    
    
    

        



