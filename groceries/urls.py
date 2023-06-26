from django.urls import path
from groceries import views


urlpatterns = [
    path('grocery/', views.GroceryItemList.as_view()),
    path('grocery/<int:pk>/', views.GroceryItemDetail.as_view()),
]
