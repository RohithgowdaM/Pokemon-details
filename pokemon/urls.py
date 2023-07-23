from django.contrib import admin
from django.urls import path
from pokemon import views
from django.conf.urls.static import static
from django.conf import settings

app_name="pokemon"

urlpatterns = [
    path("",views.home,name="pokemon"),
    path("pokefeaname",views.pokefeaname,name="pokefeaname"),
    path("pokefea",views.pokefea,name="pokefea"),
    path("upload",views.upload,name="upload")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
