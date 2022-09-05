from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("Partners/", views.Partners, name="Partners"),
    path("Donate/", views.Donate, name="Donate"),
    path("contact/", views.contact, name="contact"),
    path("Programs/", views.Programs, name="Programs"),
    path("blog1/", views.blog1, name="blog1"),
    path("Book-event/", views.event, name="Book-event"),
    path("bootcampsignup/", views.boot, name="bootcampsignup"),
]