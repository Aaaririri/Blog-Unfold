import tempfile
from pathlib import Path

from django.core.management import call_command
from django.test import TestCase, override_settings

from .models import Post


class BuildSiteTest(TestCase):
    def test_build(self):
        media = Path(tempfile.mkdtemp())
        (media / 'x.gif').write_bytes(b'GIF89a')
        Post.objects.create(titulo='A', slug='a', conteudo='oi', publicado=True)
        Post.objects.create(titulo='R', slug='r', conteudo='x')
        out = Path(tempfile.mkdtemp()) / 'dist'
        with override_settings(MEDIA_ROOT=media):
            call_command('build_site', output=str(out), base_path='/repo/')
        self.assertTrue((out / 'posts/a/index.html').exists())
        self.assertFalse((out / 'posts/r').exists())
        self.assertTrue((out / 'media/x.gif').exists())
        self.assertTrue((out / '.nojekyll').exists())
        html = (out / 'index.html').read_text()
        self.assertIn('href="/repo/posts/a/"', html)
        self.assertIn('href="/repo/curriculo/"', html)
        self.assertTrue((out / 'estudos/index.html').exists())
