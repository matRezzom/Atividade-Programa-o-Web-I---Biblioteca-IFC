from django.contrib import admin
from .models import Categoria, Livro, Emprestimo

class EmprestimoInline(admin.TabularInline):
    model = Emprestimo
    extra = 1

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "ano", "disponivel")
    list_filter = ("categoria", "disponivel")
    search_fields = ("titulo", "autor")
    list_editable = ("disponivel",)
    inlines = [EmprestimoInline]
    actions = ["marcar_indisponivel"]

@admin.action(description="Marcar como indisponível")
def marcar_indisponivel(self, request, queryset):
    queryset.update(disponivel=False)

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("livro", "aluno", "data_retirada", "devolvido")
    list_filter = ("devolvido",)
    date_hierarchy = "data_retirada"

admin.site.register(Categoria)
admin.site.site_header = "Biblioteca IFC"
admin.site.site_title = "Biblioteca IFC"
admin.site.index_title = "Painel de controle"