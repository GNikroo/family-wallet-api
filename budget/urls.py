from django.urls import path
from budget import views

urlpatterns = [
    path('budgets/', views.BudgetList.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', views.BudgetDetail.as_view(), name='budget-detail'),
]
