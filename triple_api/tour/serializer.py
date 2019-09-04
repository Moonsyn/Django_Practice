from rest_framework import serializers 
from .models import Tour

class TourSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = Tour # 모델 설정
        fields = ('id','name','address','rate') # 필드 설정
