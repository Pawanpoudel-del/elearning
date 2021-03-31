from django.urls import path
from learn.views import CourseListView, CourseDetailView

app_name="learn"
urlpatterns =[
    path('',CourseListView.as_view(), name ='courselist'),
    path('<slug:slug>',CourseDetailView.as_view()),
    ]
