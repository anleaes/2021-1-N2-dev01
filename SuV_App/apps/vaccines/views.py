from django.shortcuts import render, get_object_or_404, redirect

from .forms import VaccinesForm
from .models import Vaccine

# Create your views here.


def add_vaccine(request):
    template_name = 'vaccines/add_vaccines.html'
    context = {}
    if request.method == 'POST':
        form = VaccinesForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vaccines:list_vaccines')
    form = VaccinesForm()
    context['form'] = form
    return render(request, template_name, context)


def list_vaccines(request):
    template_name = 'vaccines/list_vaccines.html'
    vaccines = Vaccine.objects.filter()
    context = {
        'vaccines': vaccines
    }
    return render(request, template_name, context)


def edit_vaccine(request, id_vaccine):
    template_name = 'vaccines/add_vaccines.html'
    context = {}
    vaccine = get_object_or_404(Vaccine, id=id_vaccine)
    if request.method == 'POST':
        form = VaccinesForm(request.POST, request.FILES,  instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('vaccines:list_vaccines')
    form = VaccinesForm(instance=vaccine)
    context['form'] = form
    return render(request, template_name, context)


def delete_vaccine(request, id_vaccine):
    vaccine = Vaccine.objects.get(id=id_vaccine)
    vaccine.delete()
    return redirect('vaccines:list_vaccines')
