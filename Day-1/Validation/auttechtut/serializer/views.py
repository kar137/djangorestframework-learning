from rest_framework.views import APIView
from rest_framework.response import Response

from .models import comment, Student
from serializer.serializers import CommentSerializer, StudentSerializer


class CommentSerializeView(APIView):
    def get(self, request):
        data = comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({"response":"Data has been saved"})
        return Response(serializer.errors)

class StudentSerializeView(APIView):
    def get(self, request):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({"response":"Data has been saved"})
        return Response(serializer.errors)

    