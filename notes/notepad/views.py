from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html', {})




# def logout(request):
#     logout(request)
#     # Redirect to a success page.



# @login_required
# def my_notes(request):
