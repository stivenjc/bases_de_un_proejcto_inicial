from django.contrib import admin

# Register your models here.
from apps.docker_app.models import Comidas

admin.site.register(Comidas)
