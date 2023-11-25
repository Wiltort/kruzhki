#from django.shortcuts import render
#from django.http import HttpResponse
from .models import Stud_Group, Rubric
from rest_framework import viewsets
from .serializers import Stud_GroupSerializer, RubricSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly


class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    #def perform_create(self, serializer):
    #    serializer.save(stud_groups = None)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Stud_Group.objects.all()
    serializer_class = Stud_GroupSerializer