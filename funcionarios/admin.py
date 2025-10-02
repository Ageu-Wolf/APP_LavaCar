from django.contrib import admin
from django.utils.html import format_html

from .models import Funcionario
from produtos.models import Produto


@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    fields=('nome','fone','email','funcao','data_admissao','foto','fotografia')
    list_display = ('nome','fone','email','funcao')
    readonly_fields = ['fotografia']
    search_fields = ['nome','fone']
    list_filter = ['funcao',]

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}" />', obj.foto.url)
        pass
# Register your models here.
