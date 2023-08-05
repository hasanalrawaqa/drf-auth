
from django.urls import path
from .views import SnackListView,SnackDetailsView
urlpatterns = [

    path('', SnackListView.as_view(),name='snack_list'),
    path('<int:pk>/', SnackDetailsView.as_view(),name='detail_list'),
    

]
