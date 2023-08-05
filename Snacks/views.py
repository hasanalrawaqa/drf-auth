from django.shortcuts import render
from .models import Snack
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class SnackDetailsView(RetrieveUpdateDestroyAPIView):
        queryset = Snack.objects.all()
        serializer_class = SnackSerializer
        permission_classes=[IsOwnerOrReadOnly]

class SnackListView(ListCreateAPIView):
        queryset = Snack.objects.all()
        serializer_class = SnackSerializer
        permission_classes=[AllowAny]