from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views.login_user, name='login'),

]


urlpatterns = [
    # Authentication
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register,name='register'),

    

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    

    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # Chatbot page
    path('chat/', views.chatbot_page, name='chat'),

    # IT Helpdesk Tickets
    path('ticket/', views.ticket_list, name='ticket_list'),
    path('ticket/create/', views.ticket_create, name='ticket_create'),
    path('ticket/<int:id>/', views.ticket_detail, name='ticket_detail'),
    
    path('ticket/create/', views.ticket_create, name='ticket_create'),

    # # Chat history
    path('chat/history/', views.chat_history, name='chat_history'),

    path('chat/', views.chatbot_page, name='chatbot_page'),


    # path("chat/", views.chatbot_page, name="chat"),
    # path("chatbot_api/", views.chatbot_api, name="chatbot_api"),
]
