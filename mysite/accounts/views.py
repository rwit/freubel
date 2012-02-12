from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return HttpResponse("You are logged in!!")
    
