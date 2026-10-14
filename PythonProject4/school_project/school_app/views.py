from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm


def students_view(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'school_app/students.html', {'students': students, 'form': form})


def courses_view(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'school_app/courses.html', {'courses': courses, 'form': form})


def student_detail_view(request, pk):
    student = get_object_or_404(Student, pk=pk)

    # Get courses the student is NOT registered in for the select element
    unregistered_courses = Course.objects.exclude(id__in=student.courses.all())

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course = get_object_or_404(Course, id=course_id)
            student.courses.add(course)
            return redirect('student_detail', pk=student.pk)

    context = {
        'student': student,
        'unregistered_courses': unregistered_courses,
    }
    return render(request, 'school_app/student_detail.html', context)