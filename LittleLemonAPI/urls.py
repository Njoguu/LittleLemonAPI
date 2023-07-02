from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', view=menuItems),
    path('manager-view/', view=manager_view),
    path('categories/', view=categories),
    path('api-token-auth/', obtain_auth_token),
    path('groups/manager/users', view=managers),
]