from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete, name="delete"),
    path('modify/', views.modify, name="modify"),
    path('password/', views.change_password, name="change_password"),
    path('<str:username>/', views.profile, name="profile"),
]