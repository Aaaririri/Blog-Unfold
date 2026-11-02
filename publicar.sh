#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
.venv/bin/python manage.py dumpdata blog curriculo estudos --indent 2 --output content/content.json
echo "Conteúdo exportado em content/content.json. Agora: git add -A && git commit && git push"
