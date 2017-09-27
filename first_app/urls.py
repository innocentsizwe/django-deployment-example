from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact_us', views.contact_us, name='contact_us'),
]
