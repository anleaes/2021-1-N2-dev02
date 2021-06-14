from django.shortcuts import render, get_object_or_404, redirect
from .forms import FligthForm
from .models import Flight
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_flight(request):
    template_name = 'flights/add_flight.html'
    context = {}
    if request.method == 'POST':
        form = FligthForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('flights:list_flights')
    form = FligthForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_flights(request):
    template_name = 'flights/list_flights.html'
    flights = Flight.objects.filter()
    context = {
        'flights': flights
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_flight(request, id_flight):
    template_name = 'flights/add_flight.html'
    context ={}
    flight = get_object_or_404(Flight, id=id_flight)
    if request.method == 'POST':
        form = FligthForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flights:list_flights')
    form = FligthForm(instance=flight)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_flight(request, id_flight):
    flight = Flight.objects.get(id=id_flight)
    flight.delete()
    return redirect('flights:list_flights')