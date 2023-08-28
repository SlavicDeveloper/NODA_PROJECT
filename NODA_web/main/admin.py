from django.contrib import admin
from .models import Notes
from django.contrib.auth.models import User
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ['node_id', 'doc_name', 'state_status', 'category_status', ]
    list_editable = ['state_status', 'category_status']
    list_per_page = 10
    list_filter = ['state_status']

admin.site.register(Notes, NotesAdmin)



