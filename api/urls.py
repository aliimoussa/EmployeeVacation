from django.urls import path
from .import views 
urlpatterns=[
    path('',views.apiOverView,name="api-OverView"),
    path('vacation-list/',views.vacationList,name="vacation-list"),
    path('vacation-detail/<str:pk>/',views.vacationDetail,name="vacation-detail"),
    path('vacation-create/',views.vacationCreate,name="vacation-create"),
    path('vacation-update/<str:pk>/',views.vacationUpdate,name="vacation-update"),
    path('vacation-delete/<str:pk>/',views.vacationDelete,name="vacation-delete"),
    
    path('vacation-user-api/',views.vacuser,name="vacation-user-api"),
     
]