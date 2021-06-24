from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketForm, TicketPassengerForm
from .models import Ticket, TicketPassenger, Flight

# Create your views here.
def add_ticket(request, id_client):
    template_name = 'tickets/add_ticket.html'
    context = {}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.flight = Flight.objects.get(id=id_flight)
            f.save()
            form.save_m2m()
            return redirect('tickets:list_tickets')
    form = TicketForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tickets(request):
    template_name = 'tickets/list_tickets.html'
    tickets = Ticket.objects.filter()
    ticket_passenger = TicketPassenger.objects.filter()
    flights = Flight.objects.filter()
    context = {
        'tickets': tickets,
        'ticket_passengers': ticket_passenger,
        'flights': flights
    }
    return render(request, template_name, context)

def delete_ticket(request, id_ticket):
    ticket = Ticket.objects.get(id=id_ticket)
    ticket.delete()
    return redirect('tickets:list_tickets')

def add_ticket_passenger(request, id_ticket):
    template_name = 'tickets/add_ticket_passenger.html'
    context = {}
    if request.method == 'POST':
        form = TicketPassengerForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ticket = Ticket.objects.get(id=id_ticket)      
            f.save()
            form.save_m2m()
            return redirect('tickets:list_tickets')
    form = TicketPassengerForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_ticket_passenger(request, id_ticket_passenger):
    ticket_passenger = TicketPassenger.objects.get(id=id_ticket_passenger) #pode ser isso aqui, trocar para ticketpassenger
    ticket_passenger.delete()                                              #pode ser isso aqui, trocar para ticketpassenger
    return redirect('tickets:list_tickets')

def edit_ticket_status(request, id_ticket):
    template_name = 'tickets/edit_ticket_status.html'
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
