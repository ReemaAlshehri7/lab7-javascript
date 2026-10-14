from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'enrollment_date', 'courses']
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
            'courses': forms.CheckboxSelectMultiple(),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code']