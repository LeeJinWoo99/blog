from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250) # 문자 길이 설정은 필수(charField 이용일 때)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True) #시간을 받는 DateTimeField는 자동으로 시간을 불러옴(auto_now는 어려우므로 그냥 외우기)

    def __str__(self):
        return self.title
