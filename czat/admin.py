from django.contrib import admin
from czat import models

# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(models.Message)
