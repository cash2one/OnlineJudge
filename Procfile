web: python manage.py deploy; gunicorn -w 4 manage:app --log-file=- -b 0.0.0.0:5000
worker: celery -A oj.core.tasks:celery worker
