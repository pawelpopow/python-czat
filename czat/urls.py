from django.urls import path
from czat import views

app_name = 'czat'

urlpatterns = [
    path('/', views.index, name='czat'),
]