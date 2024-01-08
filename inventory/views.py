from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Inventory
from .forms import ProductForm, InventoryForm

# Create your views here.

def dashboard(request, pk):
    items = Product.objects.filter(inventory=pk)
    inventoryItems = Inventory.objects.get(inventory_id=pk)
    if 'add' in request.POST:
        addProduct = Product.objects.get(product_id=request.POST['add'])
        addProduct.quantity += 1
        addProduct.save()
    if 'sell' in request.POST:
        sellProduct = Product.objects.get(product_id=request.POST['sell'])
        sellProduct.quantity -= 1
        sellProduct.save()
    if 'form' in request.POST:
        inventory_instance = get_object_or_404(Inventory, pk=pk)
        form = ProductForm(request.POST)
        form.instance.inventory = inventory_instance
        if form.is_valid():
            form.save()
    else:
        form = ProductForm(initial={'inventory': pk}) 
    context = {
        'items' : items,
        'form': form,
        'inventory': inventoryItems.name,
        'inventoryKey': inventoryItems.pk,
    }
    return render(request, 'dashboard.html', context)

def index(request):
    items = Inventory.objects.all()
    if 'form' in request.POST:
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InventoryForm()
    context = {
        'items' : items,
        'form': form,
    }
    return render(request, 'home.html', context)

def dashboard_delete(request, pk, pk2):
    item = Product.objects.get(product_id=pk2)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard', pk=pk)
    context = {
        'item': item,
        'inventoryKey': pk,
    }
    return render(request, 'dashboard-delete.html', context)

def dashboard_edit(request, pk, pk2):
    item = Product.objects.get(product_id=pk2)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard', pk=pk)
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard-edit.html', context)

def dashboard_edit_inventory(request, pk):
    item = Inventory.objects.get(inventory_id=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard', pk=pk)
    else:
        form = InventoryForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard-edit-inventory.html', context)

def dashboard_delete_inventory(request, pk):
    item = Inventory.objects.get(inventory_id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    context = {
        'item': item,
        'inventoryKey': pk,
    }
    return render(request, 'dashboard-delete-inventory.html', context)

