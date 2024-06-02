from django.contrib import admin
from django.utils.html import format_html
from django.forms import Textarea, TextInput

from potros.models import Noticias, Calendario, Equipo, Instagram
from potros.forms import NoticiasForm

admin.site.site_header = "Mi Panel de Administración"
admin.site.site_title = "Administración Fuengirola Potros"
admin.site.index_title = "Futbol Americano"

NO_IMG = 'No Image'

class NoticiasAdmin(admin.ModelAdmin):
    form = NoticiasForm
    list_display = ('titulo', 'fecha', 'mostrar_imagen')
    ordering = ['-fecha']
    # Para mejor legibilidad en el editor de noticias.
    # Este método es llamado automáticamente por Django a la hora de construir el formulario de edición
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['cuerpo1', 'cuerpo2']:
            # Hacemos grandes los campos del cuerpo de la noticia
            formfield.widget = Textarea(attrs={'rows': 12, 'cols': 180})
        elif db_field.name == 'titulo':
            # Nos aseguramos que el título quede más pequeño que el contenido de la noticia
            formfield.widget = TextInput(attrs={'size': 80})
        return formfield

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="150" height="100" />', obj.imagen.url)
        return NO_IMG
    
    mostrar_imagen.short_description = 'Imagen Noticia'


class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'local', 'mostrar_logo_local', 'hora', 'mostrar_logo_visitante','visitante', 'jornada')
    ordering = ['fecha']

    STD_IMG_SIZE = '<img src="{}" width="50" height="50" />'

    def mostrar_logo_local(self, obj):
        if obj.logo_local:
            return format_html(self.STD_IMG_SIZE, obj.logo_local.url)
        return NO_IMG
    mostrar_logo_local.short_description = 'Logo Local'

    def mostrar_logo_visitante(self, obj):
        if obj.logo_visitante:
            return format_html(self.STD_IMG_SIZE, obj.logo_visitante.url)
        return NO_IMG
    mostrar_logo_visitante.short_description = 'Logo Visitante'

    
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('mostrar_imagen','nombre_jugador', 'edad', 'experiencia')
    ordering = ['nombre_jugador']

    def mostrar_imagen(self, obj):
        if obj.foto_jugador:
            return format_html('<img src="{}" width="50" height="50" />', obj.foto_jugador.url)
        return NO_IMG
    mostrar_imagen.short_description = 'Foto Jugador'


class InstagramAdmin(admin.ModelAdmin):
    list_display = ('mostrar_imagen','fecha','descripcion')
    ordering = ['-fecha']

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen.url)
        return NO_IMG
    mostrar_imagen.short_description = 'Imagen Instagram'

# Register your models here.
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Instagram, InstagramAdmin)
