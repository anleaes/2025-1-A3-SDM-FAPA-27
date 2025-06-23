from django.db import models

class Usuario(models.Model):
    nome       = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    senha      = models.CharField(max_length=128)
    tipo       = models.CharField(max_length=20)  # ex: 'recrutador'
    def __str__(self): return self.nome

class Empresa(models.Model):
    nome       = models.CharField(max_length=100)
    cnpj       = models.CharField(max_length=18, unique=True)
    descricao  = models.TextField()
    site       = models.URLField(blank=True)
    usuario    = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='empresas')
    def __str__(self): return self.nome

class Vaga(models.Model):
    titulo     = models.CharField(max_length=100)
    descricao  = models.TextField()
    local      = models.CharField(max_length=100)
    salario    = models.DecimalField(max_digits=10, decimal_places=2)
    empresa    = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas')
    def __str__(self): return self.titulo

class Candidato(models.Model):
    nome       = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    telefone   = models.CharField(max_length=20)
    curriculo  = models.TextField()
    def __str__(self): return self.nome

class Candidatura(models.Model):
    data_inscricao = models.DateField(auto_now_add=True)
    status         = models.CharField(max_length=50)
    candidato      = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='candidaturas')
    vaga           = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidaturas')
    def __str__(self): return f"{self.candidato} → {self.vaga}"

class Entrevista(models.Model):
    data          = models.DateTimeField()
    local         = models.CharField(max_length=100)
    observacoes   = models.TextField(blank=True)
    modo          = models.CharField(max_length=20)  # ex: 'online', 'presencial'
    candidatura   = models.ForeignKey(Candidatura, on_delete=models.CASCADE, related_name='entrevistas')
    def __str__(self): return f"Entrevista {self.id}"

class Mensagem(models.Model):
    conteudo      = models.TextField()
    data_envio    = models.DateTimeField(auto_now_add=True)
    remetente     = models.CharField(max_length=100)
    destinatario  = models.CharField(max_length=100)
    def __str__(self): return f"Msg {self.id}"

class Feedback(models.Model):
    avaliacao     = models.CharField(max_length=50)
    comentarios   = models.TextField()
    nota          = models.IntegerField()
    entrevista    = models.OneToOneField(Entrevista, on_delete=models.CASCADE, related_name='feedback')
    def __str__(self): return f"Feedback {self.id}"
