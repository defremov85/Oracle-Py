from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from cabapp.models import Tool

from refresh import copy_data

# Create your views here.

class ToolList(ListView):
    model = Tool
    template_name = "tool_list.html"
