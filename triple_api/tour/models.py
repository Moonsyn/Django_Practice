# triple_api/tour/models.py
from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=30) # 관광지 이름
    address = models.CharField(max_length=50) # 관광지 주소
    rate = models.IntegerField() # 관광지 평점

    def __self__(self):
        return self.name
