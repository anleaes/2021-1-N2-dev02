from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExtraForm
from .models import Extra

# Create your views here.
def add_extra(request):
    template_name = 'extras/add_extra.html'
    context = {}
    if request.method == 'POST':
        form = ExtraForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('extras:list_extras')
    form = ExtraForm()
    context['form'] = form
    return render(request, template_name, context)

def list_extras(request):
    template_name = 'extras/list_extras.html'
    extras = Extra.objects.filter()
    context = {
        'extras': extras
    }
    return render(request, template_name, context)

def edit_extra(request, id_extra):
    template_name = 'extras/add_extra.html'
    context ={}
    extra = get_object_or_404(Extra, id=id_extra)
    if request.method == 'POST':
        form = ExtraForm(request.POST, instance=extra)
        if form.is_valid():
            form.save()
            return redirect('extras:list_extras')
    form = ExtraForm(instance=extra)
    context['form'] = form
    return render(request, template_name, context)

def delete_extra(request, id_extra):
    extra = Extra.objects.get(id=id_extra)
    if extra.user == request.user:
        extra.delete()
    else:
        return redirect('core:home')
    return redirect('extras:list_extra')

