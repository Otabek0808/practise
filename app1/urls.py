from django.urls import include, path

from app1.views import AntivirusListView, ProgramAddView

urlpatterns = [
    path('antivirus/', AntivirusListView.as_view(), name='programm-list'),
    path('add/', ProgramAddView.as_view(), name='add-program'),
]