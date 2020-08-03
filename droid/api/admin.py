from django.contrib import admin
from droid.api.models import Anunciante, DemandaDePecas


@admin.register(Anunciante)
class AnuncianteAdmin(admin.ModelAdmin):
    """
    AnuncianteAdmin
        list_display - Fields to be viewed in django admin
        search_fields - Fields that will be viewed for django admin search
        list_filter - Fields to be filtered
    """

    list_display = ('user', 'phone_number', 'email', 'created', 'modified')
    search_fields = ['user', 'phone_number', 'email']
    ordering = ('-created',)


@admin.register(DemandaDePecas)
class DemandaDePecasAdmin(admin.ModelAdmin):
    """
    DemandaDePecasAdmin
        list_display - Fields to be viewed in django admin
        search_fields - Fields that will be viewed for django admin search
        list_filter - Fields to be filtered
    """
    list_display = ('descricao_peca', 'endereco_entrega', 'anunciante', 'status_finalizacao')
    search_fields = ['descricao_peca', 'endereco_entrega', 'anunciante', 'status_finalizacao']
    ordering = ('-created',)
