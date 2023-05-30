from django.urls import path
from apps.users.api.api import users_api_view, user_api_view

urlpatterns = [
    path('', users_api_view, name='users_api'),
    path('<int:id>/', user_api_view, name='user_api')
]
