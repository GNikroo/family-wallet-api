from django.urls import path
from expenses import views

urlpatterns = [
    path('expenses/', views.ExpenseList.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
    path('total-expense/', views.TotalExpenseStats.as_view(),
         name="total-expense-stats"),
]
