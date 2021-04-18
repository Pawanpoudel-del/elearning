from django.urls import path
from learn.views import CourseListView, CourseDetailView, UserCreateView, login, logout_view, address, CartListView, payment, ContactListView
app_name ='learn'

urlpatterns =[
    path('',CourseListView.as_view(), name ='courselist'),
    path('<slug:slug>',CourseDetailView.as_view()),
    path('signup/', UserCreateView.as_view(), name ='signup'),
    path('login/', login, name ='login'),
    path('logout/', logout_view, name ='logout'),
    path('address/', address, name='address'),
    path('cart/', CartListView.as_view(), name = 'cartlist'),
    path('payment/', payment, name='payment'),
    path('contact/', ContactListView.as_view(), name='contact'),
    ]
    
