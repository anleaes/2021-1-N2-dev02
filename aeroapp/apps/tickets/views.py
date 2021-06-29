from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketForm, TicketExtraForm
from .models import TicketExtra
from tickets.models import Ticket
from extras.models import Extra

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


def add_ticket_extra(request, id_ticket):
    template_name = 'tickets/add_ticket_extra.html'
    context = {}
    if request.method == 'POST':
        form = TicketExtraForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ticket = Ticket.objects.get(id=id_ticket)
            f.save()
            form.save_m2m()
            return redirect('tickets:list_tickets')
    form = TicketExtraForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tickets(request):
    template_name = 'tickets/list_tickets.html'
    tickets = Ticket.objects.filter()
    tickets_extras = TicketExtra.objects.filter()
    extras = Extra.objects.filter()
    context = {
        'tickets': tickets,
        'tickets_extras': tickets_extras,
        'extras': extras,
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