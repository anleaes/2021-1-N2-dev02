from django.shortcuts import render, get_object_or_404, redirect
from .forms import CityForm
from .models import City
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_city(request):
    template_name = 'cities/add_city.html'
    context = {}
    if request.method == 'POST':
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cities:list_cities')
    form = CityForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_cities(request):
    template_name = 'cities/list_cities.html'
    cities = City.objects.filter()
    context = {
        'cities': cities
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_city(request, id_city):
    template_name = 'cities/add_city.html'
    context ={}
    city = get_object_or_404(City, id=id_city)
    if request.method == 'POST':
        form = CityForm(request.POST, request.FILES,  instance=city)
        if form.is_valid():
            form.save()
            return redirect('cities:list_cities')
    form = CityForm(instance=city)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_city(request, id_city):
    city = City.objects.get(id=id_city)
    city.delete()
    return redirect('cities:list_cities')