from django.contrib import admin
from .models import Dogovor


class DogovorAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'date', 'tel1', 'address_city', 'equip', )
    list_display_links = ('number', 'name', )
    list_filter = ('address_city',)
    search_fields = ['name', 'address_city', 'number', 'tel1', 'tel2', 'tel3']


admin.site.register(Dogovor, DogovorAdmin)
