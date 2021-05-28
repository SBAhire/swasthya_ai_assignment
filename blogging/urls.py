from django.urls import path
from blogging import views

urlpatterns = [
    path('',views.home_view),
    path('blogs',views.blogs,name='blogs'),
    path('comments',views.comments,name='comments'),
]