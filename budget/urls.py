from django.urls import path
from budget import views

urlpatterns = [
    path('budget/', views.BudgetList.as_view()),
    path('budget/<int:pk>/', views.BudgetDetail.as_view()),
    path('expense/', views.ExpenseList.as_view()),
    path('expense/<int:pk>/', views.ExpenseDetail.as_view()),
    path('receipt/', views.ReceiptList.as_view()),
    path('receipt/<int:pk>/', views.ReceiptDetail.as_view()),
]
