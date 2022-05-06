from . import views
from django.urls import path

urlpatterns = [
    path('cards/', views.CardsView.as_view()),
    path('cards/<int:id>/', views.CardView.as_view()),
    path('transactions/', views.TransactionsView.as_view())
]
