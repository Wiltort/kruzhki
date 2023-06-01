from django.shortcuts import render
from .models import Group
# Create your views here.
def index(request):
    gr = Group.objects.order_by('name')
    return render(request, 'index.html', {'gr':gr})

