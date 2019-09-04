from django.db import models

# Create your models here.

class Hotel(models.Model): 
    
    name = models.CharField(max_length=30) # 호텔 이름
    grade = models.IntegerField() # 호텔 등급
    location = models.CharField(max_length=30) # 호텔 위치
    price = models.IntegerField() # 호텔 가격
    
    def __str__(self): 
        return self.name