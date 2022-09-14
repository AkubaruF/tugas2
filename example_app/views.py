from django.shortcuts import render

from example_app.models import Person

def index(request):
    persons = Person.objects.all()
    response = {'name' : 'Akbar Firdaus', 'npm' : '2106651856', 'persons' : persons}
    return render(request, 'index.html', response)
