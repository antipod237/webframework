from webframewsgi.urls import Url
from view import Homepage, EpicMath, Hello

urlpatterns= [
    Url('^$', Homepage), 
    Url('^/math$', EpicMath),
    Url('^/hello$', Hello)
]