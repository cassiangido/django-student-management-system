
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .models import Student,Courses # Import the Student and Coarses models
from django.core.exceptions import ObjectDoesNotExist # Import ObjectDoesNotExist



def signup(request):
    if request.method == 'POST':
            username =request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                  user = User.objects.create_user(username=username, email=email, password=password1) #create a new user
                  user.save() #save the user
                  messages.success(request, "Account created successfully.") # Add success message
            return redirect('login')  # Redirect to login page or any other desired page
    else:
     return render(request, 'signup.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login to avoid shadowing
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")  # Add error message
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')  # Ensure the login page is rendered for GET requests


    
    
        
        
#def logoutStudent(request):
    #logout(request)

def password_reset(request):
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')


def student_list(request):
    # Fetch the list of students
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        classname = request.POST['classname']
        # Assuming you have a Student model to save the student details
        # from .models import Student
        student = Student.objects.create(name=name, classname=classname)
        student.save()
        messages.success(request, f"Student{student.name}  added successfully.")

        return redirect('student_list')  # Redirect to the student list page after adding
    else:
        return render(request, 'add_student.html')

def delete_student(request, id):
    # Assuming you have a Student model to delete the student
    # from .models import Student
    student = Student.objects.get(pk=id)  # Fetch the student instance  
    student.delete()
    messages.success(request, f"Student {student.name} deleted successfully.")
    return redirect('student_list')  # Redirect to the student list page after deletion
      # Placeholder for delete_student function, implement as needed
 # Redirect to the student list page after deletion

def update_student(request, student_id):
    # Assuming you have a Student model to update the student details
    # from .models import Student
     student = Student.objects.get(id=student_id)  # Fetch the student instance
     
      # Use the correct form class
     if request.method == 'POST':
        student.name = request.POST.get['name']
        student.classname = request.POST.get['classname']   
        student.save()
        messages.success(request, f"Student {student.name} updated successfully.")
        return redirect('student_list')
     else:  # Redirect to the student list page after updating
        return render(request, 'update_student.html', {'student': student})  # Render the update form with existing data
     # Placeholder for update_student function, implement as needed


def student_detail(request, student_id):
    # Assuming you have a Student model to fetch the student details
    # from .models import Student
     student = Student.objects.get(id=student_id)
     return render(request, 'student_details.html', {'student': student})
     # Placeholder for student_detail function, implement as needed

def payment(request):
    return render(request, 'pay.html')

def student_details(request, student_id):
    # Assuming you have a Student model to fetch the student details
    # from .models import Student
   # student = Student.objects.get(id=student_id)
    return render(request, 'student_details.html')
    # Placeholder for student_detail function, implement as needed

#def update_student(request, student_id):
    # Assuming you have a Student model to update the student details
    # from .models import Student
    # student = Student.objects.get(id=student_id)
    # if request.method == 'POST':
    #     student.name = request.POST['name']
    #     student.classname = request.POST['classname']
    #     student.save()
    #     messages.success(request, f"Student {student.name} updated successfully.")
    #     return redirect('student_list')  # Redirect to the student list page after updating
     #return render(request, 'update_student.html')  # Render the update form with existing data
      # Placeholder for update_student function, implement as needed   

def delete_student(request, student_id):
    # Assuming you have a Student model to delete the student
    # from .models import Student
     student = Student.objects.get(id=student_id)
     student.delete()
     messages.success(request, f"Student {student.name} deleted successfully.")
     return redirect('student_list')  # Redirect to the student list page after deletion
    # return render(request, 'delete_student.html' student:'student')  # Render the update form with existing data

def flex(request):
    return render(request, 'flex.html')


def coarses(request):
     courses=Courses.objects.all()
     return render(request, 'coarses.html', {'courses': courses})


def enroll_coarse(request):
    if request.method == 'POST':
        coarsecode = request.POST['coarsecode']
        coarsename = request.POST['coarsename']
        duration = request.POST['duration']
        fees = request.POST['fees']
        coarse = Courses.objects.create(coarsecode=coarsecode, coarsename=coarsename, duration=duration, fees=fees)
        coarse.save()
        messages.success(request, f"Coarse {coarse.coarsename} added successfully.")
        return redirect('coarses')  # Redirect to the coarse list page after adding
    else:
        return render(request, 'coarse_enrollment.html')
    

def deleteCourse(request, coursecode):
    try:
        course = Courses.objects.get(coursecode=coursecode)
        course.delete()
        messages.success(request, f"Course {course.coursename} deleted successfully.")
    except ObjectDoesNotExist:
        messages.error(request, "Course not found.")
    return redirect('courses')

def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.classname = request.POST.get('classname')
        student.save()
        messages.success(request, f"Student {student.name} updated successfully.")
        return redirect('student_list')
    else:
        return render(request, 'update_student.html', {'student': student})