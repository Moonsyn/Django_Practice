from rest_framework import serializers 
from .models import Hotel 

class HotelSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = Hotel # 모델 설정 
        fields = ('id','name','grade','location', 'price') # 필드 설정
