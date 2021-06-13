from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order

# Create your views here.
def add_order(request):
    template_name = 'orders/add_order.html'
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderForm()
    context['form'] = form
    return render(request, template_name, context)

def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = Order.objects.filter()
    context = {
        'orders': orders
    }
    return render(request, template_name, context)

def edit_order(request, id_order):
    template_name = 'orders/add_order.html'
    context ={}
    order = get_object_or_404(Order, id=id_order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:list_orders')
    form = OrderForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)

def delete_order(request, id_order):
    order = Order.objects.get(id=id_order)
    order.delete()
    return redirect('orders:list_orders')
