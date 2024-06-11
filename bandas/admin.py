from django.contrib import admin

# Register your models here.

from .models import Banda



class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Banda, BandaAdmin)

from .models import Album

admin.site.register(Album)

from .models import Musica

admin.site.register(Musica)