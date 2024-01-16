from django.contrib import admin
from .models import Empleado
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "trabajo")


admin.site.register(Empleado, EmpleadoAdmin)

