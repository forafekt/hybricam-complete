from django.shortcuts import render
from django.views.generic import DetailView

def dashboard(request):
   return render(request, template_name='core/dashboard.html')

