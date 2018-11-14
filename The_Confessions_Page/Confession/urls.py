from django.conf.urls import url
from. import views
urlpatterns=[
    url(r'^Home/$',views.Home,name="Home"),
    url(r'^Confess/$',views.add_confession,name="confess"),
]
