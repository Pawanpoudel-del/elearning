from django.urls import path
from learn.views import CourseListView, CourseDetailView, UserCreateView, login

app_name ='learn'

urlpatterns =[
    path('',CourseListView.as_view(), name ='courselist'),
    path('<slug:slug>',CourseDetailView.as_view()),
    path('signup/', UserCreateView.as_view(), name ='signup'),
    path('login/', login),
    ]
