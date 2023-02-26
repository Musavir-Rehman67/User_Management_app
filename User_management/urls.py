from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login.as_view(),name="login"),
    path('add_user/',views.add_user,name="add_user"),
    path('existing_user/',views.existing_user,name="existing_user"),
    path("update_user/<str:pk>/",views.update_user,name='update_user'),
    path('delete_user/<str:pk>/',views.delete_user,name='delete_user'),
    path('logout',views.logout,name='logout'),
]