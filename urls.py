from webframewsgi.urls import Url
from view import Homepage

urlpatterns= [
    Url('^$', Homepage), 
]