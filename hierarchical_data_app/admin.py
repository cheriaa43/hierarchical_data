from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from hierarchical_data_app.models import File

# Register your models here.
admin.site.register(File, DraggableMPTTAdmin)