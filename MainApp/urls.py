from django.urls import path, re_path
from . import views

# from django.conf.urls import url
from . import views
app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name="index" ),
    path('student/',views.student, name="student" ),
    path('stud_leave',views.stud_leave, name="stud_leave" ),
    path('request_leave',views.request_leave, name="request_leave" ),
    path('view_attendance',views.view_attendance, name="view_attendance" ),
    path('get-myattendance',views.get_myattendance, name="get_myattendance" ),
    path('view_course',views.view_course, name="view_course" ),
    path('view_stud_assign',views.view_stud_assign, name="view_stud_assign" ),
    path('submit-assign/<int:id>',views.submit_assign, name="submit_assign" ),
    path('view_leaves',views.view_leaves, name="view_leaves" ),

    path('staff/',views.staff, name="staff" ),
    path('mark_attendance/',views.mark_attendance, name="mark_attendance" ),
    path('manage_attendance/',views.manage_attendance, name="manage_attendance" ),
    path('get-attendance',views.get_attendance, name="get_attendance" ),
    path('create_assign',views.create_assign, name="create_assign" ),
    path('create_new_assign',views.create_new_assign, name="create_new_assign" ),
    path('manage_assign',views.manage_assign, name="manage_assign" ),
    path('view_assign',views.view_assign, name="view_assign" ),
    path('fetch-assign/<int:id>',views.fetch_assign, name="fetch_assign" ),
    path('fetch-stud/<int:id>',views.fetch_stud, name="fetch_stud" ),
    path('update-attendance',views.update_attendance, name="update_attendance" ),


    path('myadmin/',views.myadmin, name="myadmin" ),
    path('add_staff/',views.add_staff, name="add_staff" ),
    path('add_new_staff',views.add_new_staff, name="add_new_staff" ),
    path('manage_staff',views.manage_staff, name="manage_staff" ),
    path('delete-staff/<int:id>',views.delete_staff, name="delete_staff" ),
    path('edit-staff/<int:id>',views.edit_staff, name="edit_staff" ),
    path('update_staff_data/<int:id>',views.update_staff_data, name="update_staff_data" ),
    path('add_student/',views.add_student, name="add_student" ),
    path('add_new_student',views.add_new_student, name="add_new_student" ),
    path('manage_student',views.manage_student, name="manage_student" ),
    path('delete-student/<int:id>',views.delete_student, name="delete_student" ),
    path('edit-student/<int:id>',views.edit_student, name="edit_student" ),
    path('update_stud_data/<int:id>',views.update_stud_data, name="update_stud_data" ),
    path('add_course/',views.add_course, name="add_course" ),
    path('add_new_course',views.add_new_course, name="add_new_course" ),
    path('edit-course/<int:id>',views.edit_course, name="edit_course" ),
    path('update_course/<int:id>',views.update_course, name="update_course" ),
    path('manage_course/',views.manage_course, name="manage_course" ),
    path('delete-course/<int:id>',views.delete_course, name="delete_course" ),
    path('manage_leaves/',views.manage_leaves, name="manage_leaves" ),
    path('approve-leave/<int:id>',views.approve_leave, name="approve_leave" ),
    path('reject-leave/<int:id>',views.reject_leave, name="reject_leave" ),

    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    

]