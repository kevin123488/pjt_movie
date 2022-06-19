from django.urls import path
from . import views

app_name = 'communitys'
urlpatterns = [
    path('', views.review_list_or_create, name='index'),
    path('detail/<int:review_pk>/', views.review_detail_or_update_or_delete, name='detail'),
    path('like/<int:review_pk>/', views.like_review, name='like'),
    path('comments/<int:review_pk>/', views.create_comment, name='create_comment'),
    path('comments/<int:review_pk>/<int:comment_pk>/', views.comment_update_or_delete, name='comment_update_or_delete'),
]
