from django.urls import include, path

from app1.views import AntivirusListView, OSListView, MobileListView, CompListView, AntivirusDetailView

urlpatterns = [
    path('antivirus/', AntivirusListView.as_view(), name='antivirus-list'),
    path('os/', OSListView.as_view(), name='os-list'),
    path('kompyuter-dastur', CompListView.as_view(), name='comp-list'),
    path('mobile-dastur', MobileListView.as_view(), name='mobile-list'),
    path('<int:pk>/', AntivirusDetailView.as_view(), name='antivirus-detail'),
]