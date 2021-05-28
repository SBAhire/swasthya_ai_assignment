from django.urls import path
from blogging import views

urlpatterns = [
    path('blogs',views.blogs,name='blogs'),
    path('comments',views.comments,name='comments'),
]