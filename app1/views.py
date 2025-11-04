from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy, rev
from app1.models import Programms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings


# Create your views here.

class HomePageView(ListView):
    model = Programms
    template_name = 'home.html'
    context_object_name = 'programs'

    # def get_queryset(self):
    #     query = self.request.GET.get('q', '').strip()
    #     if query:
    #         return Programms.objects.filter(name__icontains=query)
    #     else:
    #         return Programms.objects.none()  # hech nima chiqmasin
    #
class HomePageView(ListView):
    model = Programms
    template_name = 'home.html'
    context_object_name = 'programs'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return Programms.objects.filter(name__icontains=query)
        else:
            return Programms.objects.none()  # qidiruv bo‘lmasa hech narsa chiqmasin


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
        elif category == 'mobile':
            return reverse_lazy('mobile-list')
        elif category == 'comp':
            return reverse_lazy('comp-list')
        else:
            return reverse_lazy('home')


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

class AntivirusDetailView(DetailView):
    model = Programms
    template_name = 'antivirus_detail.html'

class OSDetailView(DetailView):
    model = Programms
    template_name = 'os_detail.html'

class MobileDetailView(DetailView):
    model = Programms
    template_name = 'mobile_detail.html'

class CompDetailView(DetailView):
    model = Programms
    template_name = 'comp_detail.html'

class ProgrammDeleteView(DeleteView):
    model = Programms
    template_name = 'programms_delete.html'
    reverse_lazy('home')


import os
from django.utils.text import slugify


@csrf_exempt
def upload_image(request):
    """Rasm yuklash uchun view"""
    if request.method == 'POST':
        try:
            # Faylni olish
            uploaded_file = request.FILES.get('file')
            if not uploaded_file:
                return JsonResponse({'error': 'Fayl topilmadi'}, status=400)

            # Rasm formatlarini tekshirish
            allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp', 'image/jpg']
            if uploaded_file.content_type not in allowed_types:
                return JsonResponse({'error': 'Faqat rasm fayllari (JPG, PNG, GIF) yuklash mumkin'}, status=400)

            # Fayl hajmini tekshirish (5MB)
            if uploaded_file.size > 5 * 1024 * 1024:
                return JsonResponse({'error': 'Rasm hajmi 5MB dan kichik bo\'lishi kerak'}, status=400)

            # Fayl nomini xavfsiz qilish
            name, ext = os.path.splitext(uploaded_file.name)
            safe_name = f"{slugify(name)}_{os.urandom(4).hex()}{ext}"

            # Faylni saqlash
            file_path = default_storage.save(f'tinymce_uploads/{safe_name}', uploaded_file)

            # To'liq URL ni olish
            from django.urls import reverse
            file_url = request.build_absolute_uri(default_storage.url(file_path))

            # ✅ TINYMCE UCHUN TO'G'RI RESPONSE
            return JsonResponse({
                'location': file_url  # Tinymce aynan 'location' kalit so'zini kutadi
            })

        except Exception as e:
            return JsonResponse({'error': f'Server xatosi: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Faqat POST so\'rovi qabul qilinadi'}, status=400)