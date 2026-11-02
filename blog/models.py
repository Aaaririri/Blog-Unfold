import os

from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
import markdown


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

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

    def conteudo_html(self):
        texto = self.conteudo
        for m in self.midias.all():
            texto = texto.replace(f']({m.nome})', f']({m.arquivo.url})')
        return mark_safe(markdown.markdown(texto, extensions=['fenced_code', 'tables']))


class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='midias')
    arquivo = models.FileField(
        'imagem/GIF',
        upload_to='posts/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'webp'])],
    )
    legenda = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'mídia'
        verbose_name_plural = 'mídias'

    @property
    def nome(self):
        return os.path.basename(self.arquivo.name)

    def __str__(self):
        return self.nome
