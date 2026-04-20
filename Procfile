web: sh -c "python manage.py migrate && python manage.py load_catalog && python manage.py ensure_admin && gunicorn config.wsgi:application"
