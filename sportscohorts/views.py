from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import render
from django import forms

def home(request):
    return render(request, 'login.html')