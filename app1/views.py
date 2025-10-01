from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from app1.models import Programms

# Create your views here.
class ProgramAddView(CreateView):
    model = Programms
    template_name = 'programm_add.html'
    fields = ['category', 'name','summary','download_link', 'image']

    def get_success_url(self):
        category = self.object.category  # yangi saqlangan obyektning kategoriyasi
        if category == 'antivirus':
            return reverse_lazy('antivirus-list')  # urls.py dagi nomga qarab
        elif category == 'os':
            return reverse_lazy('os-list')
        else:
            return reverse_lazy('other-list')


class AntivirusListView(ListView):
    model = Programms
    template_name = 'antivirus_list.html'
    # context_object_name = 'programms'  # template ichida nomi

    # qidiruvni ListView ichida shunaqa yoziladi
    def get_queryset(self):
        query = self.request.GET.get('q', '')  # self.request ishlatiladi
        qs = Programms.objects.filter(category='antivirus')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

class OSListView(ListView):
    model = Programms
    template_name = 'os_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # self.request ishlatiladi
        qs = Programms.objects.filter(category='os')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

class MobileListView(ListView):
    model = Programms
    template_name = 'mobile_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        qs = Programms.objects.filter(category='mobile')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

class CompListView(ListView):
    model = Programms
    template_name = 'comp_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        qs = Programms.objects.filter(category='comp')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs