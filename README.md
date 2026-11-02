# Blog-Unfold

Blog pessoal com painel administrativo Django Unfold, publicado como site estático no GitHub Pages.
O Django roda apenas localmente (para escrever); o GitHub Pages serve o HTML gerado.

Seções: **Posts** (Markdown com imagens e GIFs), **Currículo** e **Plano de Estudos**.

## Instalação local

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py createsuperuser
.venv/bin/python manage.py runserver
```

Admin em http://127.0.0.1:8000/admin/ e site em http://127.0.0.1:8000/.

## Escrevendo conteúdo

- **Posts**: no admin, crie o post, salve, envie imagens/GIFs na seção "mídias" e cole o snippet
  exibido (`![legenda](arquivo.gif)`) no conteúdo. Marque "publicado" para ele aparecer.
- **Currículo**: um único registro, com experiências, formação, habilidades e projetos.
- **Plano de estudos**: crie planos e adicione tópicos com status e progresso.

## Publicando

O banco SQLite não vai para o Git. O conteúdo é exportado para `content/content.json`
e as mídias ficam na pasta `media/`, ambos versionados.

```bash
./publicar.sh
git add -A && git commit -m "novo conteúdo" && git push
```

A cada push na `main`, o workflow `.github/workflows/deploy.yml` carrega o conteúdo,
roda `build_site` e publica.

### Configuração única no GitHub

Em **Settings -> Pages -> Source**, escolha **GitHub Actions**.

O prefixo das URLs usa o nome do repositório (`usuario.github.io/<repo>/`). Se o repositório for
`usuario.github.io` (site na raiz), troque `SITE_BASE_PATH` no workflow por `''`.

## Gerar o site localmente

```bash
.venv/bin/python manage.py build_site --base-path /Blog-Unfold/
```

O resultado fica em `dist/`. Omita `--base-path` para domínio raiz.
