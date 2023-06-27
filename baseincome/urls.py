from django.urls import path
from baseincome import views

urlpatterns = [
    path('baseincome/', views.BaseIncomeList.as_view(), name='baseincome-detail'),
    path('baseincome/<int:pk>', views.BaseIncomeDetail.as_view(),
         name='baseincome-detail'),
]
