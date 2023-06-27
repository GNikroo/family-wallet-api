from django.urls import path
from receipts import views

urlpatterns = [
    path('receipts/', views.ReceiptList.as_view()),
    path('receipts/<int:pk>/', views.ReceiptDetail.as_view()),
    path('total-receipt/', views.TotalReceiptStats.as_view(),
         name="total-receipt-stats"),
]
