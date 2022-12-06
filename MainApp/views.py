from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from .models import Extended_user, Staff, Student,Course,Leaves, Attendance,Assignment, CreateAssign
from datetime import date

def index(request):
    return render(request, "index.html", {})

def student(request):
    if request.user.is_authenticated:
        user_data = User.objects.get(id=request.user.id)
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
            print("data checker", data_check)
        except:
            data_check = False
        if data_check.user_type == "3":
            return render(request, "student_page.html", {"user_data":user_data})
        else:
            return redirect("/")
    else:
        return redirect("/")

# students leave
def stud_leave(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "3":
            return render(request, "stud_leave.html", {})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# request stud leave
def request_leave(request):
    if request.method=="POST":
        leave_date = request.POST['leave_date']
        note = request.POST['note']

        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "3":
                curr_user =User.objects.get(id=request.user.id)
                new_request = Leaves.objects.create(user=curr_user, note=note,date=date.today(), leave_date=leave_date,leave_state="applied")
                new_request.save()
                print("New Leave Applied")

                return redirect("/student")
            else:
                return redirect("/")   
        else:
            return redirect("/")


# view attendance
def view_attendance(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "3":
            stud_course= Student.objects.filter(user=request.user.id)
            return render(request, "view_attendance.html", {"stud_course":stud_course})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# get attendance
def get_myattendance(request):
    if request.method=="POST":
        course = request.POST['course']
        date = request.POST['date']

        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "3":
                student= Student.objects.get(user=request.user.id)
                attendance = Attendance.objects.filter(student=student,course=course,date=date)
                stud_course =Student.objects.filter(user=request.user.id)
                return render(request, "view_attendance.html", {"attendance":attendance,"stud_course":stud_course})
            else:
                return redirect("/")   
        else:
            return redirect("/")

# view assign
def view_stud_assign(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "3":
            stud_courses = Student.objects.filter(user=request.user.id)
            curr_user = Student.objects.get(user=request.user.id)
            my_courses = curr_user.enrolled_courses.all()
            my_course_list=[]
            for course in my_courses:
                my_course_list.append(course)
            assignments = CreateAssign.objects.all()
            my_assign = Assignment.objects.filter(student__user=request.user.id)
            submitted_list=[]
            for rec in my_assign:
                if rec.assign_state=="submitted" or rec.assign_state=="checked" or rec.assign_state=="late":
                    submitted_list.append(rec.assign.name)
            return render(request, "view_stud_assign.html", {"assignments":assignments,"stud_courses":stud_courses,"my_course_list":my_course_list,"submitted_list":submitted_list})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# submit assign
def submit_assign(request,id):
    answer= request.POST['answer']
    due_date= request.POST['due_date']
    print("date", due_date)
    print("answer", answer)
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "3":
            stud_courses = Student.objects.filter(user=request.user.id)
            rel_assign = CreateAssign.objects.get(id=id)
            curr_user = Student.objects.get(user=request.user.id)
            todays_date = date.today()
            print(type(todays_date))
            from datetime import datetime
            newdate1=datetime.strftime(datetime.strptime(due_date,'%b. %d, %Y').date(),'%Y-%m-%d')
            print("new date",type(newdate1))
            if newdate1 < str(todays_date):
                assign_state="late"
            else:
                assign_state="submitted"
            submit_assign = Assignment.objects.create(assign=rel_assign,student=curr_user,sub_date=date.today(),assign_state=assign_state,answer=answer)
            submit_assign.save()
            return redirect("/view_stud_assign")
        else:
            return redirect("/")   
    else:
        return redirect("/")


# view Course
def view_course(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "3":
            # courses= Course.objects.filter(request.user.id)
            student_course = Student.objects.filter(user=request.user.id)
            return render(request, "view_course.html", {"student_course":student_course})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# view Course
def view_leaves(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "3":
            leaves = Leaves.objects.filter(user=request.user.id)
            return render(request, "view_leaves.html", {"leaves":leaves})
        else:
            return redirect("/")   
    else:
        return redirect("/")

"""
!!!!!!!!
FOR STAFF
!!!!!!!!!!!!!
"""

def staff(request):
    if request.user.is_authenticated:
        user_data = User.objects.get(id=request.user.id)
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
            print("data checker", data_check)
        except:
            data_check = False
        if data_check.user_type == "2":
            return render(request, "staff_page.html", {"user_data":user_data})
        else:
            return redirect("/")
    else:
        return redirect("/")


# mark attendance
def mark_attendance(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            attendance = Attendance.objects.all()
            staff_course= Staff.objects.filter(user=request.user.id)
            return render(request, "mark_attendance.html", {"attendance":attendance,"staff_course":staff_course})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# fetch student
def fetch_stud(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            print(id)
            stud_list = Student.objects.filter(enrolled_courses__in=[id])
            stud_count = len(stud_list)
            staff_course= Staff.objects.filter(user=request.user.id)
            return render(request, "mark_attendance.html", {"stud_list":stud_list,"staff_course":staff_course,"stud_count":stud_count,"sel_course":id})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# update attendance
def update_attendance(request):
    if request.method=="POST":
        sel_course = request.POST['sel_course']
        date = request.POST['date']

        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "2":

                stud_count = request.POST['stud_count']
                product_dict = {}
                for i in range(1,int(stud_count)+1):
                    product_dict[f"stud_id{i}"]= request.POST[f'stud_id{i}']
                    product_dict[f"present{i}"]= request.POST.getlist(f'present{i}')

                from itertools import islice
                values = product_dict.values()
                length_to_split =  [2 for i in range(len(values)//2)]
                Inputt = iter(values)
                Output = [list(islice(Inputt, elem)) for elem in length_to_split]
                # print(Output)
                
                for rec in Output:
                    student = Student.objects.get(id=int(rec[0]))
                    course = Course.objects.get(id=int(sel_course))
                    if "on" in rec[1]:
                        att_state="1"
                    else:
                        att_state="0"
                    mark_att = Attendance.objects.create(course=course, student= student, date= date, attendance_state= att_state)
                    mark_att.save()
                    print("Attendance Saved for ",student.user.first_name)

                attendance = Attendance.objects.all()
                staff_course =Staff.objects.filter(user=request.user.id)
                return render(request, "manage_attendance.html", {"attendance":attendance,"staff_course":staff_course})
            else:
                return redirect("/")   
        else:
            return redirect("/")

# manage attendance
def manage_attendance(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            # attendance = Attendance.objects.all()
            courses= Course.objects.all()
            staff_course = Staff.objects.filter(user=request.user.id)
            return render(request, "manage_attendance.html", {"courses":courses,"staff_course":staff_course})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# get attendance
def get_attendance(request):
    if request.method=="POST":
        course = request.POST['course']
        date = request.POST['date']

        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "2":
                attendance = Attendance.objects.filter(course=course,date=date)
                staff_course = Staff.objects.filter(user=request.user.id)
                return render(request, "manage_attendance.html", {"attendance":attendance,"staff_course":staff_course})
            else:
                return redirect("/")   
        else:
            return redirect("/")

def create_assign(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            staff_course = Staff.objects.filter(user=request.user.id)
            return render(request, "create_assign.html", {"staff_course":staff_course})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# create new assign
def create_new_assign(request):
    if request.method=="POST":
        course = request.POST.get('course')
        due_date = request.POST['due_date']
        name = request.POST['assign_name']
        questions = request.POST['questions']

        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "2":
                course_inst = Course.objects.get(id=int(course))
                created_by = Staff.objects.get(user=request.user.id)
                new_assign = CreateAssign.objects.create(name=name, course=course_inst,date=date.today(), due_date=due_date,questions=questions, created_by=created_by)
                new_assign.save()
                print("New Assignment Created")
                assignments = Assignment.objects.all()
                courses =Course.objects.all()
                return render(request, "manage_assign.html", {"assignments":assignments,"courses":courses})
            else:
                return redirect("/")   
        else:
            return redirect("/")


# fetch student
def fetch_assign(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            course_inst = Course.objects.get(id=id)
            assignments = Assignment.objects.filter(assign__course=course_inst)
            staff_course= Staff.objects.filter(user=request.user.id)
            return render(request, "view_assign.html", {"staff_course":staff_course,"assignments":assignments})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# view assign
def view_assign(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            staff_course = Staff.objects.filter(user=request.user.id)
            return render(request, "view_assign.html", {"staff_course":staff_course})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# manage assign
def manage_assign(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "2":
            staff_courses = Staff.objects.filter(user=request.user.id)
            curr_user = Staff.objects.get(user=request.user.id)
            my_courses = curr_user.rel_course.all()
            my_course_list=[]
            for course in my_courses:
                my_course_list.append(course)
            assignments = CreateAssign.objects.all()
            return render(request, "manage_assign.html", {"assignments":assignments,"staff_courses":staff_courses,"my_course_list":my_course_list})
        else:
            return redirect("/")   
    else:
        return redirect("/")

"""
!!!!!!!!!!!!!!
FOR ADMIN DASHBAORD 
!!!!!!!!!!!!!!!!!!!
"""
def myadmin(request):
    if request.user.is_authenticated:
        user_data = User.objects.get(id=request.user.id)
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
            print("data checker", data_check)
        except:
            data_check = False
        if data_check.user_type == "1":
            return render(request, "admin.html", {"user_data":user_data})
        else:
            return redirect("/")
    else:
        return redirect("/")

# add staff
def add_staff(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            return render(request, "add_staff.html", {})
        else:
            return redirect("/")   
    else:
        return redirect("/")

def add_new_staff(request):
    if request.method=="POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        staff_id = request.POST['staff_id']
        rel_course = request.POST['rel_course']
        print("Rel COurse", rel_course)
        course_list =[]
        new_list = rel_course.split(",")
        for rec in new_list:
            course_list.append(int(rec))
        print("new list", course_list)


        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "1":
                user = User.objects.create_user(username=username,password= password, first_name=name)
                new_user = user.save()
                print("New User Created ID=",user.id)
                ex_user = Extended_user.objects.create(user=user, user_type="2")
                ex_user.save()
                print("Ex User Created")
                new_staff = Staff.objects.create(user=user, staff_id=staff_id)
                new_staff.rel_course.set(course_list)
                new_staff.save()
                print("New Staff Created")
                staffs = Staff.objects.all()
                return render(request, "manage_staff.html", {"staffs":staffs})
            else:
                return redirect("/")   
        else:
            return redirect("/")


# manage staff
def manage_staff(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            staffs = Staff.objects.all()
            return render(request, "manage_staff.html", {"staffs":staffs})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# delete staff
def delete_staff(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            staff = Staff.objects.get(id=id)
            staff.delete()
            staffs =Staff.objects.all()
            return render(request, "manage_staff.html", {"staffs":staffs})
        else:
            return redirect("/")   
    else:
        return redirect("/")
    

# edit staff
def edit_staff(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            staff = Staff.objects.filter(id=id)
            return render(request, "edit_staff.html", {"staff":staff})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# update staff data
def update_staff_data(request,id):
    if request.method=="POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        staff_id = request.POST['staff_id']
        rel_course = request.POST['rel_course']
        print("Rel COurse", rel_course)
        course_list =[]
        if rel_course:
            new_list = rel_course.split(",")
            for rec in new_list:
                course_list.append(int(rec))
            print("new list", course_list)


        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "1":
                user = User.objects.get(id=id)
                user.first_name = name
                user.password = password
                user.save()
                print("User Updated ID=",user.first_name)
                staff = Staff.objects.get(user=user)
                if rel_course:
                    staff.rel_course.set(course_list)
                staff.staff_id =staff_id
                staff.save()
                print("Staff Updated")
                return redirect("/manage_staff")
            else:
                return redirect("/")   
        else:
            return redirect("/")


# add student
def add_student(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            return render(request, "add_stud.html", {})
        else:
            return redirect("/")   
    else:
        return redirect("/")

def add_new_student(request):
    if request.method=="POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        stud_id = request.POST['stud_id']
        rel_course = request.POST['rel_course']
        print("Rel COurse", rel_course)
        course_list =[]
        new_list = rel_course.split(",")
        for rec in new_list:
            course_list.append(int(rec))
        print("new list", course_list)


        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "1":
                user = User.objects.create_user(username=username,password= password, first_name=name)
                new_user = user.save()
                print("New User Created ID=",user.id)
                ex_user = Extended_user.objects.create(user=user, user_type="3")
                ex_user.save()
                print("Ex User Created")
                new_stud = Student.objects.create(user=user, rollno=stud_id)
                new_stud.enrolled_courses.set(course_list)
                new_stud.save()
                print("New Staff Created")
                students = Student.objects.all()
                return render(request, "manage_stud.html", {"students":students})
            else:
                return redirect("/")   
        else:
            return redirect("/")


# manage student
def manage_student(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            students = Student.objects.all()
            return render(request, "manage_stud.html", {"students":students})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# delete student
def delete_student(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            student = Student.objects.get(id=id)
            student.delete()
            students =Student.objects.all()
            return render(request, "manage_stud.html", {"students":students})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# edit student
def edit_student(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            student = Student.objects.filter(id=id)
            return render(request, "edit_student.html", {"student":student})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# update student data
def update_stud_data(request,id):
    if request.method=="POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        stud_id = request.POST['stud_id']
        rel_course = request.POST['rel_course']
        print("Rel COurse", rel_course)
        course_list =[]
        if rel_course:
            new_list = rel_course.split(",")
            for rec in new_list:
                course_list.append(int(rec))
            print("new list", course_list)


        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "1":
                user = User.objects.get(id=id)
                user.first_name = name
                user.password = password
                user.save()
                print("User Updated ID=",user.first_name)
                student = Student.objects.get(user=user)
                if rel_course:
                    student.enrolled_courses.set(course_list)
                student.rollno =stud_id
                student.save()
                print("Student Updated")
                return redirect("/manage_student")
            else:
                return redirect("/")   
        else:
            return redirect("/")


# add_course
def add_course(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            return render(request, "add_course.html", {})
        else:
            return redirect("/")   
    else:
        return redirect("/")

def add_new_course(request):
    if request.method=="POST":
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        print("Start Date",start_date)
        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "1":
                new_course = Course.objects.create(name=name, start_date=start_date, end_date=end_date)
                new_course.save()
                print("New Course Created")
                courses = Course.objects.all()
                return render(request, "manage_course.html", {"courses":courses})
            else:
                return redirect("/")   
        else:
            return redirect("/")

# manage course
def manage_course(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            courses = Course.objects.all()
            return render(request, "manage_course.html", {"courses":courses})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# delete Course
def delete_course(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            course = Course.objects.get(id=id)
            course.delete()
            courses =Course.objects.all()
            return render(request, "manage_course.html", {"courses":courses})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# edit course
def edit_course(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            course = Course.objects.filter(id=id)
            return render(request, "edit_course.html", {"course":course})
        else:
            return redirect("/")   
    else:
        return redirect("/")
# update course
def update_course(request,id):
    if request.method=="POST":
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        print("Start Date",start_date)
        if request.user.is_authenticated:
            try:
                data_check =  Extended_user.objects.get(user = request.user.id)
            except:
                data_check = False
            if data_check.user_type == "1":
                new_course = Course.objects.get(id=id)
                new_course.name=name
                new_course.start_date=start_date
                new_course.end_date=end_date
                new_course.save()
                print(" Course Updated")
                courses = Course.objects.all()
                return redirect("/manage_course")
            else:
                return redirect("/")   
        else:
            return redirect("/")


# manage leaves
def manage_leaves(request):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            leaves = Leaves.objects.all()
            return render(request, "manage_leaves.html", {"leaves":leaves})
        else:
            return redirect("/")   
    else:
        return redirect("/")


# approve leaves
def approve_leave(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            leaves = Leaves.objects.all()
            leave_obj = Leaves.objects.get(id=id)
            leave_obj.leave_state = "approved"
            leave_obj.save()
            return render(request, "manage_leaves.html", {"leaves":leaves})
        else:
            return redirect("/")   
    else:
        return redirect("/")

# reject leaves
def reject_leave(request,id):
    if request.user.is_authenticated:
        try:
            data_check =  Extended_user.objects.get(user = request.user.id)
        except:
            data_check = False
        if data_check.user_type == "1":
            leaves = Leaves.objects.all()
            leave_obj = Leaves.objects.get(id=id)
            leave_obj.leave_state = "rejected"
            leave_obj.save()
            return render(request, "manage_leaves.html", {"leaves":leaves})
        else:
            return redirect("/")   
    else:
        return redirect("/")


"""
!!!!!!!
FOR LOGIN AND LOGOUT
!!!!!!!!!!
"""

def login(request):
    if request.method== "POST":
        username = request.POST['userid']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print(f"User {username} is loged in")
            messages.info(request,"You are successfully Loged In")
            if user_type == "1":
                return redirect("/myadmin")
            elif user_type == "2":
                return redirect("/staff")
            elif user_type == "3":
                return redirect("/student")
        else:
            messages.info(request,"Invalid Credentials!")
            print("Invalid Login detaisl")
            return redirect("/")

    else:
        return render(request, "/",{})


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")