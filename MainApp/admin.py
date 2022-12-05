from django.contrib import admin
from django.contrib.auth.models import User
from .models import Extended_user, Student, Course, Attendance, CreateAssign, Assignment, Staff, Leaves
from django.contrib.auth.admin import UserAdmin

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(CreateAssign)
admin.site.register(Assignment)
admin.site.register(Staff)
admin.site.register(Leaves)

admin.site.register(Extended_user)
# Extended user
class Extended_userInline(admin.StackedInline):
    model =Extended_user
    can_delete = False
    verbose_name_plural = 'Extended_Users' 

class CustomizedUserAdmin(UserAdmin):
    inlines = (Extended_userInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)