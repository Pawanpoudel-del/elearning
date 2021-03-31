from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from learn.models import Course
from django.utils import timezone
from django.conf import settings
from learn.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as lgin

# Create your views here.
class CourseListView(ListView):
    template_name ='learn/courselist.html'
    model=Course


class CourseDetailView(DetailView):
    template_name ='learn/coursedetail.html'
    model=Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class UserCreateView(CreateView):
    form_class =UserCreateForm
    template_name ='learn/signup.html'
    success_url =reverse_lazy('learn:courselist')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request, username=username, password=password)
    if user is not None:
       lgin(request, user)
       return render(request, 'index.html')
    else:
        pass
    return render(request, 'learn/login.html')