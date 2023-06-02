from django.shortcuts import render
from .models import Group, Rubric
# Create your views here.
def index(request):
    gr = Group.objects.order_by('name')
    return render(request, 'index.html', {'gr':gr})

#def by_rubric(request, rubric_id):
#    gr = Group.objects.filter(rubric = rubric_id)
#    return render()

