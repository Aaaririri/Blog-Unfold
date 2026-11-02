from django.db import models


class Curriculo(models.Model):
    nome = models.CharField(max_length=120)
    titulo = models.CharField('cargo/título', max_length=120, blank=True)
    resumo = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    foto = models.ImageField(upload_to='curriculo/', blank=True)
    pdf = models.FileField('PDF para download', upload_to='curriculo/', blank=True)

    class Meta:
        verbose_name = 'currículo'
        verbose_name_plural = 'currículo'

    def __str__(self):
        return self.nome


class Experiencia(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, related_name='experiencias')
    cargo = models.CharField(max_length=120)
    empresa = models.CharField(max_length=120)
    inicio = models.DateField('início')
    fim = models.DateField(null=True, blank=True, help_text='Vazio = atual')
    descricao = models.TextField('descrição', blank=True)

    class Meta:
        ordering = ['-inicio']
        verbose_name = 'experiência'
        verbose_name_plural = 'experiências'

    def __str__(self):
        return f'{self.cargo} - {self.empresa}'


class Formacao(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, related_name='formacoes')
    curso = models.CharField(max_length=120)
    instituicao = models.CharField('instituição', max_length=120)
    inicio = models.DateField('início')
    fim = models.DateField(null=True, blank=True, help_text='Vazio = em andamento')

    class Meta:
        ordering = ['-inicio']
        verbose_name = 'formação'
        verbose_name_plural = 'formações'

    def __str__(self):
        return self.curso


class Habilidade(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, related_name='habilidades')
    nome = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60, blank=True)

    class Meta:
        ordering = ['categoria', 'nome']

    def __str__(self):
        return self.nome


class ProjetoCurriculo(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE, related_name='projetos')
    nome = models.CharField(max_length=120)
    descricao = models.TextField('descrição', blank=True)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

    def __str__(self):
        return self.nome
