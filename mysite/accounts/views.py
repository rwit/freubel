from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as authlogin

@login_required
def profile(request):
    return render_to_response('user_logged_in.html', {'user':request.user})

