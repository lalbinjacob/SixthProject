from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginn,name='login'),
    path('logout',views.logout,name='logout'),
    path('main',views.logged,name='main'),
    path('order/add/', views.create_view, name='add'),
    path('order/<int:pk>/', views.update_view, name='change'),
    path('order/ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
]