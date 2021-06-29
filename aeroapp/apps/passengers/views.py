from django.shortcuts import render, get_object_or_404, redirect
from .forms import PassengerForm
from .models import Passenger
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_passenger(request):
    template_name = 'passengers/add_passenger.html'
    context = {}
    if request.method == 'POST':
        form = PassengerForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('passengers:list_passengers')
    form = PassengerForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_passengers(request):
    template_name = 'passengers/list_passengers.html'
    passengers = Passenger.objects.filter()
    context = {
        'passengers': passengers,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_passenger(request, id_passenger):
    template_name = 'passengers/add_passenger.html'
    context ={}
    passenger = get_object_or_404(Passenger, id=id_passenger)
    if request.method == 'POST':
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passengers:list_passengers')
    form = PassengerForm(instance=passenger)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_passenger(request, id_passenger):
    passenger = Passenger.objects.get(id=id_passenger)
    passenger.delete()
    return redirect('passengers:list_passengers')
