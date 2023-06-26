from django.urls import path
from .views import AccountList, AccountDetail

urlpatterns = [
    path('accounts/', AccountList.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
]
