import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path so Vercel can find your settings
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blvd.settings')

application = get_wsgi_application()

# Required by Vercel's serverless builder
app = application