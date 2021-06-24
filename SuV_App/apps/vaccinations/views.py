from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VaccinationForm
from .models import Vaccination

# Create your views here.

def add_vaccination(request):
    template_name = 'vaccinations/add_vaccination.html'
    context = {}
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vaccinations:list_vaccinations')
    form = VaccinationForm()
    context['form'] = form
    return render(request, template_name, context)

def list_vaccinations(request):
    template_name = 'vaccinations/list_vaccinations.html'
    vaccinations = Vaccination.objects.filter()
    context = {
        'vaccinations': vaccinations
    }
    return render(request, template_name, context)

def edit_vaccination(request, id_vaccination):
    template_name = 'vaccinations/add_vaccination.html'
    context ={}
    vaccination = get_object_or_404(Vaccination, id=id_vaccination)
    if request.method == 'POST':
        form = VaccinationForm(request.POST, instance=vaccination)
        if form.is_valid():
            form.save()
            return redirect('vaccinations:list_vaccinations')
    form = VaccinationForm(instance=vaccination)
    context['form'] = form
    return render(request, template_name, context)

def delete_vaccination(request, id_vaccination):
    vaccination = Vaccination.objects.get(id=id_vaccination)
    vaccination.delete()
    return redirect('vaccinations:list_vaccinations')

