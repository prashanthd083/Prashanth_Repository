from django.shortcuts import render
from datetime import datetime

# Create your views here.
def display_data(request):
    msg='HELLO PRASHANTH D HOW ARE YOU AND SERVER TIME IS GIVEN BELOW'
    server_time=datetime.now()
    dict1={'msg':msg,'server_time':server_time}
    return render(request=request,template_name='greetingapp/display.html',context=dict1)
