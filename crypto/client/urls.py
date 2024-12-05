# from django.urls import path
# from .views.brawlbots import home, create_bot

# urlpatterns = [
#     path("home", home ),
#     path("create", create_bot,  name='create_bot' ),
    
#     # path('login/', views.login_view, name='login'),
#     # path('register/', views.register_view, name='register'),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

# ]
from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import *
from .views.home import *

urlpatterns = [
    path('', home, name='home'),
    
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
