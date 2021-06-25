from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketForm, TicketPassengerForm
from .models import Ticket, TicketPassenger, Passenger, Flight

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
    tickets = Ticket.objects.filter(user=request.user)
    ticket_passengers = TicketPassenger.objects.filter()
    passengers = Passenger.objects.filter(first_name=request.user)
    flights = Flight.objects.filter()
    context = {
        'tickets': tickets,
        'ticket_passengers': ticket_passengers,
        'passengers': passengers,
        'flights': flights
    }
    return render(request, template_name, context)

def delete_ticket(request, id_ticket):
    ticket = Ticket.objects.get(id=id_ticket)
    ticket.delete()
    return redirect('tickets:list_tickets')

def delete_ticket_passenger(request, id_ticket_passenger):
    ticketpassenger = TicketPassenger.objects.get(id=id_ticket_passenger) #pode ser isso aqui, trocar para ticketpassenger
    ticketpassenger.delete()                                              #pode ser isso aqui, trocar para ticketpassenger
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
