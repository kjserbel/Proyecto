from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecordForm
from django.contrib import messages

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def register_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro guardado con éxito')
            return redirect('register_record')
        else:
            messages.error(request, 'Error al guardar el registro')
    else:
        form = RecordForm()
    return render(request, 'register_record.html', {'form': form})