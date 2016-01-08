from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AddPersonForm
from .models import Person

# Create your views here.

def index(request):
    return render(request, 'people/index.html')
    
def list(request):
    people = Person.objects.all()
    return render(request, 'people/list.html', {'people': people})
    
def add(request):
    if request.method == 'POST':
        form = AddPersonForm(request.POST)
        if form.is_valid():
            person = Person(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            person.save()
            return HttpResponseRedirect(reverse('people:list'))
    else:
        form = AddPersonForm()
         
    return render(request, 'people/add.html', {'form': form})