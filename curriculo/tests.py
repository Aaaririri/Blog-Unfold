from datetime import date

from django.test import TestCase

from .models import Curriculo


class CurriculoTest(TestCase):
    def test_vazio(self):
        self.assertContains(self.client.get('/curriculo/'), 'ainda não cadastrado')

    def test_completo(self):
        c = Curriculo.objects.create(nome='Ana', titulo='Dev')
        c.experiencias.create(cargo='Dev', empresa='X', inicio=date(2024, 1, 1))
        c.formacoes.create(curso='Eng', instituicao='UNIFEI', inicio=date(2022, 1, 1))
        c.habilidades.create(nome='Python')
        c.projetos.create(nome='Blog')
        r = self.client.get('/curriculo/')
        for t in ('Ana', 'atual', 'UNIFEI', 'Python', 'Blog'):
            self.assertContains(r, t)
