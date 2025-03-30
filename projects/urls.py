from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:id>/', views.project, name='project'),
]
