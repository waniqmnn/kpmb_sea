from django.contrib import admin
from .models import Student, Admin, Level, Category, Achievement

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Achievement)