from django.contrib import admin
from .models import Dogovor, Payment, Notification


class PaymentsInline(admin.TabularInline):
    model = Payment
    extra = 0
    min_num = 0


class DogovorAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'date', 'tel1', 'address_city', 'equip', )
    list_display_links = ('number', 'name', )
    list_filter = ('address_city',)
    search_fields = ['name', 'address_city', 'number', 'tel1', 'tel2', 'tel3']
    inlines = [PaymentsInline, ]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date', 'get_name', 'pay_type', 'amount', 'pay_place', 'comment', )
    list_display_links = ('date', 'pay_type', 'amount', 'pay_place', 'comment', )
    list_filter = ('date', 'pay_type', 'pay_place', )
    search_fields = ['date']

    def get_name(self, obj):
        return obj.dogovor_id.name
    get_name.admin_order_field = 'dogovor_id'
    get_name.short_description = 'Ф.И.О. (по договору)'


admin.site.register(Dogovor, DogovorAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Notification)
