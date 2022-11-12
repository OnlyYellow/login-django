from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login), # users/login/
    path('login/<int:id>/', views.login_detail)
]