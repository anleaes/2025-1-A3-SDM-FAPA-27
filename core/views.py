from rest_framework import viewsets
from .models import (
    Usuario, Empresa, Vaga,
    Candidato, Candidatura,
    Entrevista, Mensagem, Feedback
)
from .serializer import (
    UsuarioSerializer, EmpresaSerializer, VagaSerializer,
    CandidatoSerializer, CandidaturaSerializer,
    EntrevistaSerializer, MensagemSerializer, FeedbackSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer

class EntrevistaViewSet(viewsets.ModelViewSet):
    queryset = Entrevista.objects.all()
    serializer_class = EntrevistaSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
