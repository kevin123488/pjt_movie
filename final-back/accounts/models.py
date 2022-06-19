from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    GENRE_CHOICES = (
        (12, '모험'),
        (14, '판타지'),
        (16, '애니메이션'),
        (18, '드라마'),
        (27, '공포'),
        (28, '액션'),
        (35, '코미디'),
        (36, '역사'),
        (37, '서부'),
        (53, '스릴러'),
        (80, '범죄'),
        (99, '다큐멘터리'),
        (878, 'SF'),
        (9648, '미스터리'),
        (10402, '음악'),
        (10749, '로맨스'),
        (10751, '가족'),
        (10752, '전쟁'),
        (10770, 'TV 영화'),
    )

    genre1 = models.CharField(max_length=20, choices=GENRE_CHOICES)
    genre2 = models.CharField(max_length=20, choices=GENRE_CHOICES)
    genre3 = models.CharField(max_length=20, choices=GENRE_CHOICES)
    genre4 = models.CharField(max_length=20, choices=GENRE_CHOICES)