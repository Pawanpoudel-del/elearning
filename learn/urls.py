from django.urls import path
from learn.views import ProductListView

app_name="learn"
urlpatterns =[
    path('',ProductListView.as_view(), name ='productlist')
    ]