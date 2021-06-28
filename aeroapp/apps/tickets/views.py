from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketForm, ExtraItemForm
from .models import Ticket, Extra, ExtraItem

# Create your views here.

def add_ticket(request):
    template_name = 'tickets/add_ticket.html'
    context = {}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('tickets:list_tickets')
    form = TicketForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tickets(request):
    template_name = 'tickets/list_tickets.html'
    tickets = Ticket.objects.filter()
    extra_items = ExtraItem.objects.filter()
    extra = Extra.objects.filter()
    context = {
        'tickets': tickets,
        'extra_items': extra_items,
        'extra': extra,
    }
    return render(request, template_name, context)

def edit_ticket(request, id_ticket):
    template_name = 'tickets/add_ticket.html'
    context ={}
    ticket = get_object_or_404(Ticket, id=id_ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets:list_tickets')
    form = TicketForm(instance=ticket)
    context['form'] = form
    return render(request, template_name, context)

def delete_ticket(request, id_ticket):
    ticket = Ticket.objects.get(id=id_ticket)
    ticket.delete()
    return redirect('tickets:list_tickets')


def add_extra_item(request, id_extra):
    template_name = 'extras/add_extra_item.html'
    context = {}
    if request.method == 'POST':
        form = ExtraItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.extra = Extra.objects.get(id=id_extra)
            f.user = request.user            
            f.save()
            form.save_m2m()
            return redirect('extras:list_extras')
    form = ExtraItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_extra_item(request, id_extra_item):
    extraitem = ExtraItem.objects.get(id=id_extra_item)
    extraitem.delete()
    return redirect('extras:list_extras')