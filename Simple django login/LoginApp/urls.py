from django.urls import path
from . import views
app_nem = 'LoginApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('home/<userinfo>', views.home, name='home')
]