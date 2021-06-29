from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from .forms import VaccinationForm
from .models import Vaccination

# Create your views here.
#Adiciona vacinação
@login_required(login_url='/contas/login/')
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

#Lista vacinação
@login_required(login_url='/contas/login/')
def list_vaccinations(request):
    template_name = 'vaccinations/list_vaccinations.html'
    vaccinations = Vaccination.objects.filter()
    context = {
        'vaccinations': vaccinations
    }
    return render(request, template_name, context)

#Edita vacinação
@login_required(login_url='/contas/login/')
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

#Deleta vacinação
@login_required(login_url='/contas/login/')
def delete_vaccination(request, id_vaccination):
    vaccination = Vaccination.objects.get(id=id_vaccination)
    vaccination.delete()
    return redirect('vaccinations:list_vaccinations')

#Lista nova vacinação
@login_required(login_url='/contas/login/')
def edit_vaccination_status(request, id_vaccination):
    template_name = 'vaccinations/status_vaccination.html'
    context ={}
    vaccination = get_object_or_404(Vaccination, id=id_vaccination)
    if request.method == 'POST':
        form = VaccinationForm(request.POST, instance=vaccination)
        if form.is_valid():
            f = form.save(commit=False)
            f.vaccination = Vaccination.objects.get(id=id_vaccination)
            f.save()
            form.save_m2m()
            return redirect('vaccinations:list_vaccinations')
    form = VaccinationForm(instance=vaccination)
    context['form'] = form
    return render(request, template_name, context)


#Lista vacinação status
@login_required(login_url='/contas/login/')
def list_vaccinations_status(request):
    template_name = 'vaccinations/list_vaccinations.html'
    vaccinations = Vaccination.objects.filter()
    context = {
        'vaccinations': vaccinations
    }
    return render(request, template_name, context)