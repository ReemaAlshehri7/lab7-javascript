from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_view, name='students'),
    path('courses/', views.courses_view, name='courses'),
    path('student/<int:pk>/', views.student_detail_view, name='student_detail'),
]