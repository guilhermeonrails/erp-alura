from django.contrib import admin
from contatos.models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome','email', 'cargo', 'telefone')
    ordering = ('nome',)
    search_fields = ('nome',)