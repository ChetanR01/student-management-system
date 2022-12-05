from django.db import models
from django.contrib.auth.models import User
from datetime import date
"""
Models For Student
"""
# Courses
class Course(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Student 
class Student(models.Model):
    user = models.ForeignKey(User,  related_name='student', on_delete=models.CASCADE)
    rollno = models.CharField(max_length=10)
    enrolled_courses = models.ManyToManyField(to=Course,  related_name='enroll_course', blank=True)

    def __str__(self):
        return self.user

# Students attendance
class Attendance(models.Model):
    course = models.ForeignKey(Course, related_name='course_attend', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_attend', on_delete=models.CASCADE)
    date = models.DateField()
    Attendance_status = (("1", "Present"), ("0", "Absent"))
    attendance_state = models.CharField(choices=Attendance_status, max_length=1)
    
    def __str__(self):
        return f"{self.course}({self.date})"



"""
Models For Staff
"""
# staff 
class Staff(models.Model):
    user = models.ForeignKey(User,  related_name='staff', on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=10)
    rel_course = models.ManyToManyField(to=Course,  related_name='staff_course', blank=True)


    def __str__(self):
        return self.staff_id


# create assignment
class CreateAssign(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course,  related_name='course_assign', on_delete=models.CASCADE)
    date = models.DateField()
    questions = models.TextField()
    due_date = models.DateField()
    created_by = models.ForeignKey(Staff,  related_name='created_by', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Students Assignment submitted
class Assignment(models.Model):
    assign = models.ForeignKey(CreateAssign,  related_name='sub_assign', on_delete=models.CASCADE)
    student = models.ForeignKey(Student,  related_name='student_assign', on_delete=models.CASCADE)
    sub_date = models.DateField(default=date.today())
    answer = models.TextField()
    Assign_status = (("submitted", "Submitted"), ("notsubmitted", "Not Submitted"), ("checked", "Checked"), ("late", "Delayed"))
    assign_state = models.CharField(choices=Assign_status, max_length=50)
    
    def __str__(self):
        return f"{self.sub_date}-{self.assign_state}"


# Leaves
class Leaves(models.Model):
    user = models.ForeignKey(User, related_name='user_leave', on_delete=models.CASCADE)
    date = models.DateField()
    leave_date = models.DateField()
    note = models.TextField()
    leave_option = (("applied", "Applied"), ("approve", "Approve"), ("reject", "Reject"))
    leave_state = models.CharField(choices=leave_option, max_length=50)

    # def __str__(self):
    #     return self.user


# Extend user model
class Extended_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE = (('1', "Admin"), ('2', "Staff"), ('3', "Student"))
    user_type = models.CharField(choices=USER_TYPE, max_length=1)

   