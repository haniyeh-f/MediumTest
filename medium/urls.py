from django.urls import path

from medium import views

urlpatterns = [
    path('articles', views.api_view),
]
