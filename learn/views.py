from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from learn.models import Course
from django.utils import timezone
from django.conf import settings
from learn.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as lgin, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Cart, Address, OrderedCourse, Course, Contact
from django.core.paginator import Paginator
import datetime
import requests
from django.core.mail import send_mail

# Create your views here.
class CourseListView(ListView):
    template_name ='learn/courselist.html'
    paginate_by=1
    model=Course

class CartListView(ListView):
     template_name='learn/cart.html'
     model= Cart

class CourseDetailView(DetailView):
    template_name ='learn/coursedetail.html'
    model=Course

    def post(self, request, slug, *args, **kwargs):
        if request.POST.get('quantity')!= None :
            username = request.user
            item = get_object_or_404(Course, slug = slug)
            quantity = request.POST.get('quantity')
            if Cart.objects.filter(item = item).exists():
                obj = get_object_or_404(Cart, item = item)
                obj.quantity = obj.quantity+ int(quantity)
                obj.save()
                return redirect('learn:address')
            else:
                y = Cart(user = username, item = item, quantity = quantity)
                y.save()
                return redirect('learn:address')
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

def address(request):
    if request.POST.get('city') is not None:
        username = request.user
        pradesh = request.POST.get('pradesh')
        city = request.POST.get('city') 
        country = request.POST.get('country')
        contact_number = request.POST.get('contact-number')
        s = Address(user= username, pradesh=pradesh, city= city, country=country, contact_number= contact_number)
        s.save()
        return redirect('learn:payment')
    cart_data = Cart.objects.filter(user=request.user)
    return render(request, 'learn/address.html', {'data': cart_data})


class Payment(DetailView):
    template_name ='learn/payment.html'
    model=Cart

def payment(request):
    sum =0
    for x in Cart.objects.filter(user = request.user):
        sum = sum+x.item.price*x.quantity
    if request.POST.get('payment_method') == "red":
        username = request.user
        item =Cart.objects.filter(user =username)
        #address =Address.objects.get(user =username)
        address =Address.objects.filter(user =username).order_by('-id')[0]
        s = OrderedCourse(user =username, address = address, ordered_date =datetime.datetime.now(), ordered = True, sum =sum*100, payment_choices= 'COD')
        s.save()
        s.item.set =item
        s.save()
        return redirect('learn:courselist')
    elif request.POST.get('payment_method') == "blue":
        token = request.POST.get('token')
        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
        "token": token,
        "amount": 1000
        }
        headers = {
        "Authorization": "Key live_secret_key_970b77a215224e0482282023a35abe2a"
        }

        response = requests.post(url, payload, headers = headers)
        username = request.user
        item =Cart.objects.filter(user =username)
        #address =Address.objects.get(user =username)
        address =Address.objects.filter(user =username).order_by('-id')[0]
        s = OrderedCourse(user =username, address = address, ordered_date =datetime.datetime.now(), ordered = True, sum =sum*100, payment_choices= 'ONLINE', payment = True)
        s.save()
        s.item.set =item
        s.save()
        send_mail(
            'Ordered Successfully. Thank you for ordering courses through this platform.',
            'You have successfully purchased a course.',
            settings.EMAIL_HOST_USER,
            [request.user.email],
            fail_silently=False,
        )
        return redirect('learn:courselist')
    return render(request, 'learn/payment.html', {'data': sum*100})
    
class ContactListView(ListView):
     template_name='learn/contact.html'
     model= Contact

     def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        s= Contact(name=name, email=email, message=message)
        s.save()
        return render(request, 'learn/contact.html')
        

