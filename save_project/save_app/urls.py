from django.urls import path
from save_app import views

app_name = 'save_app'

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
    # path('login', views.login, name = 'login')
]
