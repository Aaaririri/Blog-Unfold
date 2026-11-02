from django.core.validators import MaxValueValidator
from django.db import models


class PlanoEstudo(models.Model):
    titulo = models.CharField('área/objetivo', max_length=120)
    descricao = models.TextField('descrição', blank=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem', 'titulo']
        verbose_name = 'plano de estudo'
        verbose_name_plural = 'planos de estudo'

    def __str__(self):
        return self.titulo

    def progresso(self):
        topicos = list(self.topicos.all())
        if not topicos:
            return 0
        return round(sum(t.progresso for t in topicos) / len(topicos))


class Topico(models.Model):
    class Status(models.TextChoices):
        PLANEJADO = 'planejado', 'Planejado'
        ANDAMENTO = 'andamento', 'Em andamento'
        CONCLUIDO = 'concluido', 'Concluído'

    plano = models.ForeignKey(PlanoEstudo, on_delete=models.CASCADE, related_name='topicos')
    titulo = models.CharField('título', max_length=160)
    descricao = models.TextField('descrição', blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PLANEJADO)
    progresso = models.PositiveIntegerField(
        'progresso (%)', default=0, validators=[MaxValueValidator(100)]
    )
    inicio = models.DateField('início', null=True, blank=True)
    fim = models.DateField(null=True, blank=True)
    link = models.URLField('link/recurso', blank=True)

    class Meta:
        ordering = ['inicio', 'id']
        verbose_name = 'tópico'
        verbose_name_plural = 'tópicos'

    def save(self, *args, **kwargs):
        if self.status == self.Status.CONCLUIDO:
            self.progresso = 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
