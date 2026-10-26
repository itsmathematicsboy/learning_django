from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Mengarahkan ke fungsi index di polls/views.py
    path("<int:question_id>/", views.detail)
]