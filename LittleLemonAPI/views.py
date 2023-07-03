from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.
class MenuItemView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    search_fields = ['title']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]


class SingleItemView(generics.RetrieveUpdateDestroyAPIView, generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' \
                or self.request.method == 'DELETE' or self.request.method == 'PATCH':
            return [IsAdminUser()]
        return [AllowAny()]


class CategoryView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['title']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        if self.request.method == 'POST':  
            return [IsAdminUser()]
        return [AllowAny()]


class ManagerUsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # Get Managers
        manager_group = Group.objects.get(name='Manager')
        # Get users in the Managers group
        queryset = User.objects.filter(groups=manager_group)
        return queryset

    def perform_create(self, serializer):
        # Assign a user to Managers
        manager_group = Group.objects.get(name='Manager')
        user = serializer.save()
        user.groups.add(manager_group)


class ManagerSingleUserView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # Get the 'Manager' group
        manager_group = Group.objects.get(name='Manager')
        # Get the users in the 'Manager' group
        queryset = User.objects.filter(groups=manager_group)
        return queryset


class Delivery_crew_management(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        queryset = User.objects.filter(groups=delivery_crew)
        return queryset

    def perform_create(self, serializer):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        user = serializer.save()
        user.groups.add(delivery_crew)


class Delivery_crew_management_single_view(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        queryset = User.objects.filter(groups=delivery_crew)
        return queryset


class Customer_Cart(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def perform_create(self, serializer):
        menuitem = self.request.data.get('menuitem')
        quantity = self.request.data.get('quantity')
        unit_price = MenuItem.objects.get(pk=menuitem).price
        quantity = int(quantity)
        price = quantity * unit_price
        serializer.save(user=self.request.user, price=price)

    def delete(self, request):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response(status=204)


class Orders_view(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def perform_create(self, serializer):
        cart_items = Cart.objects.filter(user=self.request.user)
        total = self.calculate_total(cart_items)
        order = serializer.save(user=self.request.user, total=total)

        for cart_item in cart_items:
            OrderItem.objects.create(menuitem=cart_item.menuitem, quantity=cart_item.quantity,
                                     unit_price=cart_item.unit_price, price=cart_item.price, order=order)
            cart_item.delete()

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        return Order.objects.filter(user=user)


    def calculate_total(self, cart_items):
        total = Decimal(0)
        for item in cart_items:
            total += item.price
        return total


class Single_Order_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        return Order.objects.filter(user=user)