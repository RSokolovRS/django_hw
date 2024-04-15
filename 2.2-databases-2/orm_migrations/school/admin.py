from django.contrib import admin

from .models import Student, Teacher, Enrollment


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['name', 'group']
    inlines = [EnrollmentInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['name', 'subject']
    inlines = [EnrollmentInline, ]
