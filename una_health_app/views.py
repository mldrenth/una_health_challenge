from django.shortcuts import render
from una_health_app.models import *

from django.http import HttpResponse

def index(request):
    users = User.objects.all()
    if request.method == "POST":
        form_data = request.POST
        user_id = form_data['user_id']
        user = User.objects.get(user_id = user_id)
        glucose_values = GlucoseValue.objects.filter(user_id = user.id)
        
           
        return render(request, 'una_health_app/userdata.html', locals())
    else:
        return render(request, 'una_health_app/index.html', locals())

