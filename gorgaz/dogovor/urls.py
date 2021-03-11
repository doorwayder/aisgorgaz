from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('city-autocomplete/', views.city_autocomplete, name='city-autocomplete'),
    path('street-autocomplete/', views.street_autocomplete, name='street-autocomplete'),
    path('dogovor/<int:dogovor_id>/', views.dogovor_view, name='dogovor'),
    path('dogovor/<int:dogovor_id>/update/', views.dogovor_update, name='update'),
    path('add/', views.dogovor_add, name='add'),
    path('dogovor/<int:dogovor_id>/newpay/', views.dogovor_newpay, name='newpay'),
    path('dogovor/<int:dogovor_id>/updatepay/', views.dogovor_updatepay, name='updatepay'),
    path('search/', views.dogovor_search, name='search'),
    path('address/', views.dogovor_search_address, name='search_address'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('convert/', views.convert),
]
