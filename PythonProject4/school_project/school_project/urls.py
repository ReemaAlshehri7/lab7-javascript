from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <-- Import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('students')),  # <-- Redirects root to students path
    path('', include('school_app.urls')),
]