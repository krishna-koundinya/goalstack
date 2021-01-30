from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Goal

class GoalListView(ListView):
    model = Goal