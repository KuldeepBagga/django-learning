from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
# Create your views here.
from . import models

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    
class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='class_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School
    
class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('class_app:list')

class IndexView(TemplateView):
    template_name='index.html'
    

        
        