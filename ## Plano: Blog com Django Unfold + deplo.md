## Plano: Blog com Django Unfold + deploy no GitHub Pages

**Arquitetura (ponto-chave)**: o GitHub Pages só serve arquivos estáticos. Então o Django (com Unfold) roda **localmente como painel de administração** (onde você cria posts, currículo e plano de estudos), e um comando gera o **site estático** (HTML/CSS/mídia) numa pasta `docs/`/branch publicada pelo GitHub Actions.

### 1. Estrutura
- Projeto Django `config/` + apps `blog`, `curriculo`, `estudos`
- `requirements.txt`: django, django-unfold, pillow, markdown (ou django-ckeditor/unfold wysiwyg), django-distill (ou comando próprio de geração estática)
- SQLite local (db versionado ou exportado via fixtures para você não perder conteúdo)

### 2. Modelos (administrados via Unfold)
- **Post**: título, slug, resumo, capa, conteúdo em Markdown, data, publicado (bool), tags. Imagens e GIFs via modelo `PostMedia` (inline no admin, upload de png/jpg/gif/webp) referenciáveis no Markdown; GIFs são copiados sem processamento para preservar animação.
- **Curriculo** (singleton): resumo, contato/links, PDF opcional para download; inlines de `Experiencia`, `Formacao`, `Habilidade`, `Projeto`.
- **Estudos**: `PlanoEstudo` (área/objetivo) -> `Topico` (título, descrição, status: planejado/em andamento/concluído, datas início/fim, progresso %, links/recursos). Página mostra linha do tempo/barra de progresso para evidenciar evolução.

### 3. Admin com Unfold
- Configurar `UNFOLD` (título, menu lateral com seções Blog / Currículo / Estudos, dashboard simples com contagem de posts e progresso de estudos)
- Inlines, filtros, `ModelAdmin` do Unfold, campo de edição Markdown com pré-visualização

### 4. Site público (templates)
- Base com navegação: **Início/Posts**, **Currículo**, **Plano de Estudos**; CSS leve (Tailwind CDN ou CSS próprio), responsivo
- Páginas: lista de posts, detalhe do post (Markdown renderizado com imagens/GIFs), currículo (com botão imprimir/PDF), estudos (agrupado por plano, status e progresso)

### 5. Geração estática
- Comando `python manage.py build_site` que renderiza todas as páginas em `dist/`, copia `static/` e `media/`, usa URLs relativas/`BASE_URL` configurável (necessário para `usuario.github.io/repositorio/`), gera `.nojekyll`

### 6. Deploy
- Workflow `.github/workflows/deploy.yml`: em push na `main`, instala dependências, roda `build_site` e publica com `actions/deploy-pages`. Como o banco precisa estar disponível no CI, o conteúdo é versionado (SQLite + `media/` no repo, ou fixtures JSON).
- Fluxo: editar no admin local -> `git push` -> site atualiza.

### 7. Extras
- `.gitignore`, `README.md` em português com passos (venv, migrate, createsuperuser, runserver, build, configurar Pages em Settings -> Pages -> GitHub Actions)
- Verificação: rodar migrações, criar dados de exemplo, executar `build_site` e conferir os arquivos HTML gerados.

**Suposições**: Markdown para conteúdo; SQLite versionado no repo; site em português. Me diga se prefere outro editor de texto ou outro modo de guardar o conteúdo.