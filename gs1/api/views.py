from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Model Object - Single Student Data

def student_detail(request,pk):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu)

          # Or we can write a single line code for render the data 

        return JsonResponse(serializer.data)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type = 'application/json')

# Query Set - All student  dataset
def student_list(request):
        stu = Student.objects.all()

        serializer = StudentSerializer(stu,many = True)

        # json_data = JSONRenderer().render(serializer.data)

        # return HttpResponse(json_data, content_type = 'application/json')

        # or we can write a single line code for render the data 

        return JsonResponse(serializer.data,safe = False)

