from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from learn.models import Course
from django.utils import timezone
from django.conf import settings
from learn.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as lgin, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Cart
from django.core.paginator import Paginator

# Create your views here.
class CourseListView(ListView):
    template_name ='learn/courselist.html'
    paginate_by=1
    model=Course


class CourseDetailView(DetailView):
    template_name ='learn/coursedetail.html'
    model=Course

    def post(self, request, slug, *args, **kwargs):
        if request.POST.get('quantity')!= None :
            username = request.user
            item = get_object_or_404(Course, slug = slug)
            quantity = request.POST.get('quantity')
            y = Cart(user = username, item = item, quantity = quantity)
            y.save()
            return render(request, 'index.html')
        return render(request, 'learn/cart.html')


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

def logout_view(request):
    logout_msg ="Logout Successfully"
    logout(request)
    return render(request, 'index.html', {'data':logout_msg})