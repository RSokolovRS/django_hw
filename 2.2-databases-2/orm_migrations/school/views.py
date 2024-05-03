from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().order_by('group')
    # teachers = Teacher.students.objects.all()
    # teachers = Teacher.objects.get(students__id=3)
    for stu in students:
        for tea in stu.teachers.all():
            print(f'Студент {stu.name}: Преподователь {tea.name}')
        # print(stu)
    context = {
        'students': students,
        # 'teachers': teachers
    }


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
