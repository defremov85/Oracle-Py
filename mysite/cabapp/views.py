from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic.list import ListView

from cabapp.models import Tool

from refresh import copy_data
from refresh import truncate_table

# Create your views here.

class ToolList(ListView):
    model = Tool
    template_name = "tool_list.html"

def cp(request):
    if(request.POST.get('refresh')):
        copy_data.copy_data()
        response = TemplateResponse(request, 'cabapp/refresh.html', {})
    #return HttpResponse('Refresh is in progress...!')
    return response

def truncate(request):
    if(request.POST.get('truncate')):
        truncate_table.truncate_table()
    return HttpResponse('Truncated...!')