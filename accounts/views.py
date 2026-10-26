from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pet_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form, 'title':'чужакам тут не рады !'}) # 



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)
            return redirect('pet_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
        'title': "Чужак, докажи что ты из наших!",
    })