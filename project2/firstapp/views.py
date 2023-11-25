from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def display_data(request):
    msg="hi prashanth"
    server_time=datetime.datetime.now()
    data1='<h1>'+msg+'</h1>'
    data2 = '<h2>'+str(server_time)+'</h1>'
    data3=data1+data2
    return HttpResponse(data3)
