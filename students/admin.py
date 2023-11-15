from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'grade')
    search_fields = ('name', 'grade')

admin.site.register(Student, StudentAdmin)
