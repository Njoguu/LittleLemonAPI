from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from .serializers import MenuItemSerializer, CategorySerializer

# Create your views here.

# The admin can add menu items
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def menuItems(request):
    if request.method == 'GET':
        return Response({"message": "this is the menu-item"})
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)
    
# The admin can add categories
@api_view(['POST'])
@permission_classes([IsAdminUser])
def categories(request):
    serialized_item = CategorySerializer(data=request.data)
    serialized_item.is_valid(raise_exception=True)
    serialized_item.save()
    return Response(serialized_item.data, status=status.HTTP_201_CREATED)
    
@api_view()
@permission_classes([IsAuthenticated, IsAdminUser])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Only Manager should see this!"})
    else:
        return Response({"message": "You are not authorized"}, 403)

# admin can assign users to the manager group
@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User,username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({"message": "OK!"})
    
    return Response({"message": "Error!"}, 400)
