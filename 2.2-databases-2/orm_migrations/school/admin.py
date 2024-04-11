from django.contrib import admin

from .models import Student, Teacher, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 3

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ist_display = ['id', 'name', 'group']
    list_filter = ['name', 'group']
    inlines = [EnrollmentInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['name', 'subject']
    inlines = [EnrollmentInline, ]
