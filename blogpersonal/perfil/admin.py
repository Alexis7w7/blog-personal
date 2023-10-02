from django.contrib import admin
from .models import Project


# Register your models here.
# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created')
    list_editable = ('title',)
    list_filter = ('title', 'created', 'update')
    search_fields = ('title',)
