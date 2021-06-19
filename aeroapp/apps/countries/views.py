from django.shortcuts import render, get_object_or_404, redirect
from .forms import CountryForm
from .models import Country

# Create your views here.
def add_country(request):
    template_name = 'countries/add_country.html'
    context = {}
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('countries:list_countries')
    form = CountryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_countries(request):
    template_name = 'countries/list_countries.html'
    countries = Country.objects.filter()
    context = {
        'countries': countries
    }
    return render(request, template_name, context)

def edit_country(request, id_country):
    template_name = 'countries/add_country.html'
    context ={}
    country = get_object_or_404(Country, id=id_country)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('countries:list_countries')
    form = CountryForm(instance=country)
    context['form'] = form
    return render(request, template_name, context)

def delete_country(request, id_country):
    country = Country.objects.get(id=id_country)
    country.delete()
    return redirect('countries:list_countries')
