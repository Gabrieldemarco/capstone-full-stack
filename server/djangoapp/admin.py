from django.contrib import admin
from .models import CarMake, CarModel

# Permite que los modelos de CarModel se muestren dentro de CarMake en el panel de administración
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Permite agregar modelos de autos directamente en la vista de CarMake

# Configuración de CarMake en el panel de administración
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Muestra estos campos en la vista de lista
    search_fields = ('name',)
    inlines = [CarModelInline]  # Agrega los modelos de autos dentro de cada fabricante

# Configuración de CarModel en el panel de administración
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Campos a mostrar
    list_filter = ('car_make', 'type', 'year')  # Agrega filtros laterales
    search_fields = ('name', 'car_make__name')  # Permite buscar por nombre o fabricante

# Registrar los modelos en el panel de administración
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
