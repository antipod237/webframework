import os
from webframewsgi.main import WebFrame
from urls import urlpatterns

settings = {
    'BASE_DIR': os.path.dirname(os.path.abspath(__file__)),
    'TEMPLATE_DIR_NAME': 'templates'
}

app=WebFrame(
    urls = urlpatterns,
    settings = settings
)