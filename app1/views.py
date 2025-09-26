
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from app1.models import Programms


# Create your views here.
class ProgramAddView(CreateView):
    model = Programms
    template_name = 'programm_add.html'
    fields = ['name','summary','document']

    def get_success_url(self):
        return reverse_lazy('programm-list')

class AntivirusListView(ListView):
    model = Programms
    template_name = 'antivirus_list.html'