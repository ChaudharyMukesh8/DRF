from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
        # validator
        def start_with_r(value):
              if value[0].lower() != 'r':
                   raise serializers.ValidationError('name should be start with R')
        name = serializers.CharField(validators=[start_with_r])
        
        class Meta:
               model = Student
               fields  = ['name','roll','city']
        

        
        #Field level validation
        def validate_roll(self,value):
               if  value >= 200:
                     raise serializers.ValidationError('Seat Full')
               return value
        
        # Object Level validation
        def validate(self,data):
               nm = data.get('name')
               ct = data.get('city')
               if nm.lower() == 'veera' and ct.lower() != 'gkp':
                      raise serializers.ValidationError('city must be GKP')
               return data
        
        

