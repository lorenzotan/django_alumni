from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'alumni'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^students/$', views.students, name='students'),

    url(r'^(?P<student_id>[0-9]+)/$', views.student, name='student'),
]
