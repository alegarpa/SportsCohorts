from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from django.views.decorators.csrf import csrf_exempt
import json

from messagePost.models import messagePost

from django.shortcuts import render
from django import forms

# GET requests

# will delete this later--just a sanity check
def index(request):
    return HttpResponse("Hello, world. You're at the messagePost index.")