from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from app.forms import *


# Create your views here.
class Templatehtml(TemplateView):
    template_name='Templatehtml.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='prasanth'
        ECDO['from']='chittoor-AP'
        return ECDO
    
# Form by using Template View
    
class InsertschoolbyTV(TemplateView):
    template_name='InsertschoolbyTV.html'
    def get_context_data(self,**kwargs):
        ESDO=super().get_context_data(**kwargs)
        ESDO['SFO']=SchoolForm
        return ESDO
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertschoolbyTV is Done')
        
# Form by using Form View Class
           
class InsertschoolbyFV(FormView):
    template_name='InsertschoolbyFV.html'
    form_class=SchoolForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertschoolbyFV is Done')