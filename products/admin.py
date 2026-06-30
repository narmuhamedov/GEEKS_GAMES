from django.contrib import admin
from . import models

admin.site.register(models.Hero)
admin.site.register(models.Person)
admin.site.register(models.ReviewHero)
admin.site.register(models.FightLocation)

