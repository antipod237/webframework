from webframewsgi.main import WebFrame
from urls import urlpatterns

app=WebFrame(
    urls=urlpatterns
)