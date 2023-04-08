from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    
    path('add-vacation/', views.addVacation, name='add-vacation'),
    path('edit-vacation/<str:id>', views.editVacation, name='edit-vacation'),
    path('delete-vacation/<str:id>', views.deleteVacation, name='delete-vacation'),
  
  
    path('approve-vacation/<str:id>', views.approve, name='approve-vacation'),
    path('deny-vacation/<str:id>', views.deny, name='deny-vacation'),

    path('vacation-user/', views.showUserVacation, name='vacation-user'),
]