from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostoForm
from .models import Posto

# Create your views here.
def add_posto(request):
    template_name = 'posto/add_posto.html'
    context = {}
    if request.method == 'POST':
        form = PostoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('posto:list_postos')
    form = PostoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_postos(request):
    template_name = 'posto/list_postos.html'
    postos = Posto.objects.filter()
    context = {
        'posto': postos
    }
    return render(request, template_name, context)

def edit_posto(request, id_posto):
    template_name = 'posto/add_posto.html'
    context ={}
    posto = get_object_or_404(Posto, id=id_posto)
    if request.method == 'POST':
        form = PostoForm(request.POST, instance=posto)
        if form.is_valid():
            form.save()
            return redirect('posto:list_postos')
    form = PostoForm(instance=posto)
    context['form'] = form
    return render(request, template_name, context)

def delete_posto(request, id_posto):
    posto = Posto.objects.get(id=id_posto)
    posto.delete()
    return redirect('posto:list_postos')