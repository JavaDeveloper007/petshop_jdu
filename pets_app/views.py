from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet
from .forms import PetForm

# Create your views here.

from django.views.generic import ListView
# # # Old
# class PetListView(ListView):
#     model = Pet
#     template_name = 'pets_app/pet_list.html'
#     context_object_name = 'pets'

class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pets_app/pet_list.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return Pet.objects.select_related('category')
    

# # # Old
# def pet_list(request):
#     pets = Pet.objects.all()
#     return render(request, 'pets_app/pet_list.html', {'pets': pets})

@login_required
def pet_list(request):
    pets = Pet.objects.select_related('category').all()
    return render(request, 'pets_app/pet_list.html', {'pets': pets})


@login_required
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets_app/pet_detail.html', {'pet': pet})

@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets_app/pet_form.html', {'form': form})


