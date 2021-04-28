from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('export', views.dogovor_export_excel, name='dogovor_export'),
    path('notifyexport', views.notification_export_excel, name='notification_export'),
    path('cities/', views.cities_stats, name='cities'),
    path('dogovors/', views.dogovors, name='dogovors'),
    path('payments/', views.payments, name='payments'),
    path('plan/', views.plan, name='plan'),
    path('orders/', views.orders, name='orders'),
    path('printorder/<int:order_id>/', views.order_print, name='printorder'),
    path('neworder/', views.order_add, name='neworder'),
    path('order/<int:order_id>/', views.order_update, name='order'),
    path('delorder/<int:order_id>/', views.order_delete, name='delorder'),
    path('inactive/', views.dogovor_inactive, name='inactive'),
    path('expired/', views.dogovor_expired, name='expired'),
    path('datepayments/', views.payments_by_date, name='datepayments'),
    path('namepayments/', views.payments_by_name, name='namepayments'),
    path('numpayments/', views.payments_by_number, name='numpayments'),
    path('city-autocomplete/', views.city_autocomplete, name='city-autocomplete'),
    path('street-autocomplete/', views.street_autocomplete, name='street-autocomplete'),
    path('name-autocomplete/', views.name_autocomplete, name='name-autocomplete'),
    path('dogovor/<int:dogovor_id>/', views.dogovor_view, name='dogovor'),
    path('dogovor/<int:dogovor_id>/update/', views.dogovor_update, name='update'),
    path('doc1/<int:dogovor_id>/', views.dogovor_doc1, name='doc1'),
    path('doc2/<int:dogovor_id>/', views.dogovor_doc2, name='doc2'),
    path('doc3/<int:dogovor_id>/', views.dogovor_doc3, name='doc3'),
    path('doc4/<int:dogovor_id>/', views.dogovor_doc4, name='doc4'),
    path('doc5/<int:dogovor_id>/', views.dogovor_doc5, name='doc5'),
    path('add/', views.dogovor_add, name='add'),
    path('dogovor/<int:dogovor_id>/newpay/', views.dogovor_newpay, name='newpay'),
    path('updatepay/<int:payment_id>/', views.dogovor_updatepay, name='updatepay'),
    path('delpay/<int:payment_id>/', views.payment_delete, name='delpay'),
    path('search/', views.dogovor_search, name='search'),
    path('name/', views.dogovor_search_name, name='name'),
    path('address/', views.dogovor_search_address, name='search_address'),
    path('notifications/', views.notifications, name='notifications'),
    path('addnotifications/', views.add_notifications, name='addnotifications'),
    path('updatenotify1/', views.update_notify1, name='updatenotify1'),
    path('updatenotify2/', views.update_notify2, name='updatenotify2'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
