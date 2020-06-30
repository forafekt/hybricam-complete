from django.conf.urls import url

from pages import views

app_name = "pages"
urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^about/$", views.about, name="about"),
]
