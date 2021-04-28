from django.contrib import admin
from .models import Dogovor, Payment, Notification, Worker, Order, Plan


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


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'dogovor_id', 'create_time', 'send_time_1', 'success_1', 'send_time_2', 'success_2')
    list_display_links = ('dogovor_id', )
    list_filter = ('create_time',)

    def get_name(self, obj):
        return obj.dogovor_id.name
    get_name.short_description = 'Ф.И.О. (по договору)'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'job', 'date', )
    list_display_links = ('id', 'name', 'address')
    list_filter = ('date',)


admin.site.register(Dogovor, DogovorAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Worker)
admin.site.register(Order, OrderAdmin)
admin.site.register(Plan)
