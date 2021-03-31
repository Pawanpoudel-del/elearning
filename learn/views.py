from django.shortcuts import render
from django.views.generic import ListView, DetailView
from learn.models import Course
from django.utils import timezone

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
