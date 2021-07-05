from django.urls import path

from . import views

app_name = 'person'
urlpatterns = [
    path('', views.create_person_data, name='create_person'),
    path('<int:pk>/', views.update_person_data, name='update_person'),
    path('reminder/', views.reminder, name='reminder'),
]
