from django.urls import path, re_path
from . import views

urlpatterns = [
    path('city-autocomplete/', views.city_autocomplete, name='city-autocomplete'),
    path('', views.main, name='main'),
    path('dogovor/<int:dogovor_id>/', views.dogovor_view, name='dogovor'),
    path('dogovor/<int:dogovor_id>/update/', views.dogovor_update, name='update'),
    path('add/', views.dogovor_add, name='add'),
    path('search/', views.dogovor_search, name='search'),
    path('address/', views.dogovor_search_address, name='search_address'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('convert/', views.convert),
]
