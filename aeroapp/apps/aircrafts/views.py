from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import AircraftForm
from .models import Aircraft

# Create your views here.
@login_required(login_url='/contas/login/')
def add_aircraft(request):
    template_name = 'aircrafts/add_aircraft.html'
    context = {}
    if request.method == 'POST':
        form = AircraftForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('aircrafts:list_aircrafts')
    form = AircraftForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_aircrafts(request):
    template_name = 'aircrafts/list_aircrafts.html'
    aircrafts = Aircraft.objects.filter()
    context = {
        'aircrafts': aircrafts
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_aircraft(request, id_aircraft):
    template_name = 'aircrafts/add_aircraft.html'
    context ={}
    aircraft = get_object_or_404(Aircraft, id=id_aircraft)
    if request.method == 'POST':
        form = AircraftForm(request.POST, instance=aircraft)
        if form.is_valid():
            form.save()
            return redirect('aircrafts:list_aircrafts')
    form = AircraftForm(instance=aircraft)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_aircraft(request, id_aircraft):
    aircraft = Aircraft.objects.get(id=id_aircraft)
    aircraft.delete()
    return redirect('aircrafts:list_aircrafts')
