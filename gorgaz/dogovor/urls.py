from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dogovor/<int:dogovor_id>/', views.dogovor_view, name='dogovor'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('convert/', views.convert),
]
