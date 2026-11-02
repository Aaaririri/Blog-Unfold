from django.test import TestCase

from .models import PlanoEstudo


class EstudosTest(TestCase):
    def test_vazio(self):
        self.assertContains(self.client.get('/estudos/'), 'Nenhum plano')

    def test_progresso_e_pagina(self):
        p = PlanoEstudo.objects.create(titulo='Python')
        p.topicos.create(titulo='Básico', status='concluido')
        p.topicos.create(titulo='Django', status='andamento', progresso=50)
        self.assertEqual(p.progresso(), 75)
        r = self.client.get('/estudos/')
        for t in ('Python', 'Básico', 'Em andamento', '75%'):
            self.assertContains(r, t)
