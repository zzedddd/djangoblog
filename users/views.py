from django.shortcuts import render
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):

    def post(self, request):
        form = UserRegisterForm(request.POST)
        return render(request, 'users/register.html', {'form': form})

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
