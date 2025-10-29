"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# from django.views.generic.base import TemplateView
from app1.views import HomePageView, ProgrammDeleteView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # 🔄 tilni almashtirish uchun
]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('programms/', include('app1.urls')),
    path('admin-panel/', ProgrammDeleteView.as_view(), name='delete'),
    path('tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


