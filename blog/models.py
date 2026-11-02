from django.db import models
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField('título', max_length=200)
    slug = models.SlugField(unique=True)
    resumo = models.CharField(max_length=300, blank=True)
    capa = models.ImageField(upload_to='capas/', blank=True)
    conteudo = models.TextField('conteúdo (Markdown)')
    publicado_em = models.DateTimeField('data', default=timezone.now)
    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-publicado_em']

    def __str__(self):
        return self.titulo
