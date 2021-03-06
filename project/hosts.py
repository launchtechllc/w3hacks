from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'home.urls', name='www'),
    host(r'app', 'app.urls', name='app'),
    host(r'hackathon', 'hackathon.urls', name='hackathon'),
    host(r'links', 'links.urls', name='links'),
    host(r'blog', 'blog.urls', name='blog'),
)
