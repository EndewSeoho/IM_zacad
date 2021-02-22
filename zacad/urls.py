from django.urls import path
from . import views

app_name = 'zacad'

urlpatterns = (
    path('', views.IMView.as_view()),
    path('<int:index>', views.IMView.as_view())
)