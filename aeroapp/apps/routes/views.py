from django.shortcuts import render, get_object_or_404, redirect
from .forms import RouteForm
from .models import Route
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_route(request):
    template_name = 'routes/add_route.html'
    context = {}
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('routes:list_routes')
    form = RouteForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_routes(request):
    template_name = 'routes/list_routes.html'
    routes = Route.objects.filter()
    cities = City.objects.filter()
    context = {
        'routes': routes,
        'cities': cities
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_route(request, id_route):
    template_name = 'routes/add_route.html'
    context ={}
    route = get_object_or_404(Route, id=id_route)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('routes:list_routes')
    form = RouteForm(instance=route)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_route(request, id_route):
    route = Route.objects.get(id=id_route)
    route.delete()
    return redirect('routes:list_routes')
