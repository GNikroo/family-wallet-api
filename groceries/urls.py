from django.urls import path
from groceries import views

urlpatterns = [
    path('groceries/', views.GroceryItemList.as_view()),
    path('groceries/<int:pk>/', views.GroceryItemDetail.as_view()),
    path('total-grocery-expense/', views.TotalGroceryExpenseStats.as_view(),
         name="total-expense-stats"),
]
