from django.contrib import admin
from agenda.models import Eventos


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_event', 'data_criacao')
    #ira chama o display no objeto criado
    list_filter = ('data_event', 'titulo')

admin.site.register(Eventos,EventoAdmin)