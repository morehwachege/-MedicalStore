from django.urls import path
from Users import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('new_user/', views.create_user, name="new_user"),
]
