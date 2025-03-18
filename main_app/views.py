from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import PlayFound

## AUTHORIZATION
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

### Imports for the signup!
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    error_message = ''
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('playfounds-index')
        else: 
            error_message = "Invalid sign up - try again"
    
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


@login_required
def playfounds_index(request):
    playfounds = PlayFound.objects.filter(user=request.user)
    return render(request, 'playfounds/index.html', {'playfounds': playfounds})


@login_required
def playfound_detail(request, pk):
    playfound = get_object_or_404(PlayFound, pk=pk)
    activities = playfound.activities.all()
    return render(request, 'playfounds/detail.html', {
        'playfound': playfound,
        'activities': activities
    })
    

class PlayFoundCreate(LoginRequiredMixin, CreateView):
    model = PlayFound
    fields = ['name', 'location', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlayFoundUpdate(LoginRequiredMixin, UpdateView):
    model = PlayFound
    fields = ['name', 'location', 'description']


class PlayFoundDelete(LoginRequiredMixin, DeleteView):
    model = PlayFound
    success_url = '/playfounds/'


class SuggestionCreate(CreateView):
    model = PlayFound
    fields = ['location', 'description', 'name', 'image']
    template_name = 'suggestion_form.html'


class SuggestionUpdate(UpdateView):
    model = PlayFound
    fields = ['location', 'description', 'name', 'image']
    template_name = 'suggestion_form.html'


class SuggestionDelete(DeleteView):
    model = PlayFound
    success_url = reverse_lazy('playfounds-index')
    template_name = 'suggestion_confirm_delete.html'
    
