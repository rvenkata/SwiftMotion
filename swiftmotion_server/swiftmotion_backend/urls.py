from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.csv_view, name='csv_upload_view'),
    url(r'^upload/csv$', views.upload_csv, name='upload_csv')
]
