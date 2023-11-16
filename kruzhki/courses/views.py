from django.shortcuts import render
from django.http import HttpResponse
from .models import Stud_Group
# Create your views here.

def index(request):
    gr = Stud_Group.objects.all()[:10]
    output = []
    for item in gr:
        output.append(item.name)
    return HttpResponse('\n'.join(output))