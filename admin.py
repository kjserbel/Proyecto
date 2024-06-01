from django.contrib import admin
from .models import Record

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'casilla', 'votosmorenapvpt', 'votosmc', 'votospripanprd')
    search_fields = ('seccion', 'casilla')

    def imagen_tag(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
        return "No Image"

    imagen_tag.short_description = 'Imagen'
    
admin.site.register(Record, RecordAdmin)