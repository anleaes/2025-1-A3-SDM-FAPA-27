"""
URL configuration for RecrutamentoSelecao project.

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
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'recrutadores', views.RecrutadorViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'vagas', views.VagaViewSet)
router.register(r'candidatos', views.CandidatoViewSet)
router.register(r'candidaturas', views.CandidaturaViewSet)
router.register(r'entrevistas', views.EntrevistaViewSet)
router.register(r'mensagens', views.MensagemViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
