from django.shortcuts import render, get_object_or_404, redirect
from .forms import StateForm
from .models import State
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_state(request):
    template_name = 'states/add_state.html'
    context = {}
    if request.method == 'POST':
        form = StateForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('states:list_states')
    form = StateForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_states(request):
    template_name = 'states/list_states.html'
    states = State.objects.filter()
    context = {
        'states': states
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_state(request, id_state):
    template_name = 'states/add_state.html'
    context ={}
    state = get_object_or_404(State, id=id_state)
    if request.method == 'POST':
        form = StateForm(request.POST, request.FILES,  instance=state)
        if form.is_valid():
            form.save()
            return redirect('states:list_states')
    form = StateForm(instance=state)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_state(request, id_state):
    state = State.objects.get(id=id_state)
    state.delete()
    return redirect('states:list_states')
