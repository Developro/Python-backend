from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^questions/$', questions),
    url(r'^questions/(?P<pk>[0-9]+)/$', question_detail),
]
