from django.shortcuts import HttpResponse, get_object_or_404, render, HttpResponseRedirect
from .models import Pet
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    pets = Pet.objects.all()
    template = loader.get_template('index.html')
    context = {
        'pet_list': pets
    }
    return HttpResponse(template.render(context, request))

def pet(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pet.html', {'pet': pet})

def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        if request.POST['name'] == '' or request.POST['description'] == '':
            return render(request, 'add.html', {'error_message': "You must fill all field"})

        pet = Pet()
        pet.name = request.POST['name']
        pet.description = request.POST['description']
        pet.save()
        return HttpResponseRedirect(reverse('index'))
