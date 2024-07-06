from django.contrib import admin
from apps.formula.models import Formula
# import html safe
from django.utils.safestring import mark_safe
    
@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variables', 'formula2', 'code', 'formula_img', 'file']
    list_display_links = ['name']
    search_fields = ['name', 'variables', 'formula', 'code']
    list_filter = ['name', 'variables', 'formula', 'code']
    readonly_fields = ['variables', 'formula_img']
    list_per_page = 10
    list_max_show_all = 100
    
    def formula2(self, obj):
        return mark_safe(obj.formula)