from django.contrib import admin

from .models import Equipamento


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'tipo', 'classe_risco', 'data_aquisicao', 'ativo')
    search_fields = ('nome', 'codigo', 'tipo', 'classe_risco')
    list_filter = ('ativo', 'tipo', 'classe_risco')
