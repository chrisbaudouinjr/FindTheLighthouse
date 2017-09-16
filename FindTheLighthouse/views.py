from django.shortcuts import render
from django.contrib.auth.models import User


# Main landing page of the site
def index(request):

    return render(request, 'index.html', context={"user": request.user})

# View for "Find Your People"
def people(request):
    return render(request, 'people.html')


# View for "Meet Up"
def meetup(request):
    return render(request, 'meetup.html')
