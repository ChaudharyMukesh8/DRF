from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
        # city = serializers.CharField(read_only=True)
        class Meta:
                model = Student
                fields = ['name','roll','city']
                # to make more than one field read only
                # read_only_fields = ['name','roll']
                # or
                extra_kwargs = {'name':{'read_only':True}}
