from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
