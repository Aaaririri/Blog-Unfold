import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.test import Client, override_settings
from django.urls import reverse, set_script_prefix

from blog.models import Post


class Command(BaseCommand):
    help = 'Gera o site estático em dist/ (ou --output).'

    def add_arguments(self, parser):
        parser.add_argument('--output', default=str(settings.BASE_DIR / 'dist'))
        parser.add_argument(
            '--base-path',
            default=settings.SITE_BASE_PATH,
            help='Prefixo das URLs, ex.: /meu-repo/ (vazio para domínio raiz)',
        )

    def handle(self, *args, **opts):
        base = opts['base_path'].strip('/')
        set_script_prefix(f'/{base}/' if base else '/')
        out = settings.BASE_DIR.joinpath(opts['output'])
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)

        urls = [reverse('blog:lista'), reverse('curriculo:pagina'), reverse('estudos:pagina')]
        urls += [p.get_absolute_url() for p in Post.objects.filter(publicado=True)]

        client = Client(HTTP_HOST='localhost')
        prefix = f'/{base}' if base else ''
        for url in urls:
            path = url[len(prefix):]
            with override_settings(ALLOWED_HOSTS=['localhost']):
                resp = client.get(path)
            if resp.status_code != 200:
                raise CommandError(f'{path} retornou {resp.status_code}')
            dest = out / path.lstrip('/') / 'index.html'
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(resp.content)

        if settings.MEDIA_ROOT.exists():
            shutil.copytree(settings.MEDIA_ROOT, out / 'media')
        (out / '.nojekyll').touch()
        self.stdout.write(self.style.SUCCESS(f'{len(urls)} páginas geradas em {out}'))
