import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newspaper_agency.settings")

application = get_wsgi_application()
