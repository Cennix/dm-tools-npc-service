from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.NpcDetails.as_view()),
    path('graph/nodes', views.NpcGraphNodes.as_view()),
    path('graph/links', views.NpcGraphLinks.as_view()),
]