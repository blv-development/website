from django.shortcuts import render
from .models import Developer

def developer_list(request):
    developers = Developer.objects.all()
    return render(request, 'devs_list.html', {'developers': developers})