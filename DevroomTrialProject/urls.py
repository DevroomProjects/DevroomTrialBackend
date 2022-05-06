from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('api/', include('accounts.urls')),
    path('api/', include('cards.urls'))
]
