# apiRestDjangoDockerizado

Primer proyecto con Django: API CRUD de frases (`phrases`, Django REST Framework) con
admin de Django. Requiere Python 3 + Django/DRF instalados.

## Cómo correr en local
```bash
cd MiPagina2
python manage.py migrate
python manage.py runserver   # http://localhost:8000
```

> Nota: pese al nombre del repo, no incluye `Dockerfile` ni `docker-compose` — corre
> directo con Python.
