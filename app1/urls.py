from django.urls import include, path

from app1.views import (
    AntivirusListView,
    OSListView,
    MobileListView,
    CompListView,
    AntivirusDetailView,
    OSDetailView,
    MobileDetailView,
    CompDetailView,
)

urlpatterns = [
    path('antivirus/', AntivirusListView.as_view(), name='antivirus-list'),
    path('os/', OSListView.as_view(), name='os-list'),
    path('kompyuter-dastur', CompListView.as_view(), name='comp-list'),
    path('mobile-dastur', MobileListView.as_view(), name='mobile-list'),
    path('/antivirus/<int:pk>/', AntivirusDetailView.as_view(), name='antivirus-detail'),
    path('/kompyuter-dastur/<int:pk>/', CompDetailView.as_view(), name='comp-detail'),
    path('/mobile-dastur/<int:pk>/', MobileDetailView.as_view(), name='mobile-detail'),
    path('os/<int:pk>/', OSDetailView.as_view(), name='os-detail'),
]