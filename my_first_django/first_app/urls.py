from django.conf.urls import include
from first_app import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index,name="index"),

]
