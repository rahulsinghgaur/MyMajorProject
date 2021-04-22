from django.contrib import admin
from django.urls import path
from notes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("login/", views.loginUser, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("about/", views.about, name="about"),
    path("downloadnotes/", views.downloadnotes, name="downloadnotes"),
    path("impupdate/", views.impupdate, name="impupdate"),
    path("downloadsection/", views.downloadsection, name="downloadsection"),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)