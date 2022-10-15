from django.contrib import admin
from apps.school.models import Course, Student, Enrollment


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'rg', 'cpf')
    list_per_page = 20


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    search_fields = ('code',)
    list_per_page = 20


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'student', 'period')
    list_display_links = ('id', )
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
