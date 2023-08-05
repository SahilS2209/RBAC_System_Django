from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
    path('add_api/', views.add_api, name='add_api'),
    path('update_api/<int:api_id>/', views.update_api, name='update_api'),
    path('delete_api/<int:api_id>/', views.delete_api, name='delete_api'),
    path('view_api/', views.view_api, name='view_api'),
    
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.remove_user, name='delete_user'),
    path('view_users/', views.view_users, name='view_users'),
    
    path('map/', views.map_api_to_user, name='map'),
    # path('v_u_api/', views.view_apis_for_user, name='v_u_api'),
    
    
]