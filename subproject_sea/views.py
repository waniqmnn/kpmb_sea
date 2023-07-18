from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Level, Category, Achievement, Admin
from django.contrib import messages
from django.http import HttpResponseBadRequest,HttpResponse;

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def deletedata_student(request, student_id):
    if not request.session.get('Studentid'):
        return redirect('login')

    # Retrieve the currently logged-in student
    logged_in_student_id = request.session['Studentid']
    logged_in_student = get_object_or_404(Student, Studentid=logged_in_student_id)

    # Retrieve the student to be deleted
    student_to_delete = get_object_or_404(Student, Studentid=student_id)

    if logged_in_student.Studentname != student_to_delete.Studentname or logged_in_student.Studentid != student_to_delete.Studentid:
        messages.error(request, "You don't have permission to delete this student.")
        return redirect('viewachievement')

    # Delete the student
    student_to_delete.delete()

    messages.success(request, "Student deleted successfully.")
    return redirect('viewachievement')

def deleteachievement(request, achievement_id):
    # Retrieve the achievement to be deleted
    achievement_to_delete = get_object_or_404(Achievement, id=achievement_id)

    # Delete the achievement
    achievement_to_delete.delete()

    messages.success(request, "Achievement deleted successfully.")
    return redirect('viewachievement')


def loginstudents(request):
    if request.method == 'POST':
        studentid = request.POST.get('Studentid')
        spassword = request.POST.get('Spassword')

        try:
            student = Student.objects.get(Studentid=studentid)
            if student.Spassword == spassword:
                request.session['Studentid'] = student.Studentid
                return HttpResponse('success')  # Return a success response
        except Student.DoesNotExist:
            pass

        return HttpResponseBadRequest('Invalid student ID or password')  # Return an error response

    return render(request, 'loginstudents.html')

def registerstudents(request):
    if request.method == 'POST':
        studentid = request.POST.get('Studentid', '')
        student_name = request.POST.get('Studentname', '')
        student_password = request.POST.get('Spassword', '')
        student_programme = request.POST.get('Studentprogramme', '')
        student_phone = request.POST.get('Studentphone', '')
        try:
            student = Student.objects.create(Studentid=studentid, Studentname=student_name, Spassword=student_password, Studentprogramme=student_programme, Studentphone=student_phone)
            request.session['Studentid'] = student.Studentid
            return redirect('loginstudents')
        except Exception as e:
            error_message = str(e)
            return render(request, 'registerstudents.html', {'error_message': error_message})
    return render(request, 'registerstudents.html')


def loginadmin(request):
    if request.method == 'POST':
        adminid = request.POST['adminid'] 
        apassword = request.POST['apassword']  # Provide a default value if the key is missing

        try:
            admin = Admin.objects.get(adminid=adminid, apassword=apassword)
            if admin.apassword == apassword:
                # Set a session variable to indicate the user is logged in
                request.session['adminid'] = admin.adminid
                return redirect('viewachievement')  # Redirect to the admin dashboard page
            else:
                error_message = 'Invalid password.'
        except Admin.DoesNotExist:
            error_message = 'Admin does not exist.'

        return render(request, 'loginadmin.html', {'error_message': error_message})

    return render(request, 'loginadmin.html')

def registeradmin(request):
    if request.method == 'POST':
        adminid = request.POST.get('adminid', '')
        name = request.POST.get('name', '')
        apassword = request.POST.get('apassword', '')
        phone_number = request.POST.get('phone_number', '')

        try:
            admin = Admin.objects.create(adminid=adminid, name=name, apassword=apassword, phone_number=phone_number)
            request.session['adminid'] = admin.adminid
            return redirect('loginadmin')
        except Exception as e:
            error_message = str(e)
            return render(request, 'registeradmin.html', {'error_message': error_message})
    return render(request, 'registeradmin.html')

def viewachievement(request):
    achievements = Achievement.objects.all()
    context={
        'alldata' : achievements
    }
    return render(request, 'viewachievement.html', context)

def viewachievementforstudent(request):
    achievements = Achievement.objects.all()
    context={
        'alldata' : achievements
    }
    return render(request, 'viewachievementforstudent.html', context)

def create_achievment(request):
    if request.method == 'POST':
        student_id = request.POST.get('Studentid')
        level_id = request.POST.get('Levelid')
        category_id = request.POST.get('Categoryid')
        award = request.POST.get('Award')
        achievement_date = request.POST.get('Achievement_date')
        event = request.POST.get('Event')

        if not (student_id and level_id and category_id and award and achievement_date and event):
            return redirect('missing_fields')

        try:
            student = Student.objects.get(Studentid=student_id)
            level = Level.objects.get(Levelid=level_id)
            category = Category.objects.get(Categoryid=category_id)
        except Student.DoesNotExist:
            return redirect('student_not_found')
        except Level.DoesNotExist:
            return redirect('level_not_found')
        except Category.DoesNotExist:
            return redirect('category_not_found')

        achievement = Achievement(
            Studentid=student,
            Levelid=level,
            Categoryid=category,
            Award=award,
            Achievement_date=achievement_date,
            Event=event
        )
        achievement.save()

        return redirect('viewachievement')

    levels = Level.objects.all()
    categories = Category.objects.all()
    context = {'levels': levels, 'categories': categories}
    return render(request, 'achievment_form.html', context)

def create_level(request):
    if request.method == 'POST':
        level_id = request.POST['Levelid']
        level_description = request.POST['Leveldescription']

        # Create the Level object and save it to the database
        level = Level.objects.create(
            Levelid=level_id,
            Leveldescription=level_description
        )

        # Redirect to a success page or any other relevant view
        return redirect('viewachievement')

    levels = Level.objects.all()

    return render(request, 'level_form.html', {'levels': levels})

def create_category(request):
    if request.method == 'POST':
        category_id = request.POST['Categoryid']
        category_description = request.POST['Categorydescription']

        # Create the Category object and save it to the database
        category = Category.objects.create(
            Categoryid=category_id,
            Categorydescription=category_description
        )

        # Redirect to a success page or any other relevant view
        return redirect('viewachievement')

    categories = Category.objects.all()

    return render(request, 'category_form.html', {'categories': categories})

def admindata(request):
     if 'adminid' in request.session:
        admin_id = request.session['adminid']
        admin = Admin.objects.get(adminid=admin_id)
        context = {'admin': admin}
        return render(request, 'admindata.html', context)
     else:
        return redirect('registeradmin')
    
def searchpage(request):
    query = request.GET.get('query', '')

    if query:
        students = Student.objects.filter(Studentname__icontains=query) | Student.objects.filter(Studentid__icontains=query)
        if not students:
            error_message = f"No results found for '{query}'."
            return render(request, 'searchpage.html', {'error_message': error_message})
    else:
        students = []

    return render(request, 'searchpage.html', {'students': students})

def searchpageforstudent(request):
    query = request.GET.get('query', '')

    if query:
        students = Student.objects.filter(Studentname__icontains=query) | Student.objects.filter(Studentid__icontains=query)
        if not students:
            error_message = f"No results found for '{query}'."
            return render(request, 'searchpageforstudent.html', {'error_message': error_message})
    else:
        students = []

    return render(request, 'searchpageforstudent.html', {'students': students})

def updateadmin(request, admin_id):
    admin = get_object_or_404(Admin, adminid=admin_id)

    if request.method == 'POST':
        phone = request.POST['phone']
        admin.phone_number = phone
        admin.save()

        return redirect('viewachievement')

    context = {
        'admin': admin,
    }

    return render(request, 'updateadmin.html', context)

def studentdata(request):
    if 'Studentid' in request.session:
        student_id = request.session['Studentid']
        try:
            student = Student.objects.get(Studentid=student_id)
            context = {'student': student}
            return render(request, 'studentdata.html', context)
        except Student.DoesNotExist:
            return render(request, 'viewachievement.html')
    else:
        return redirect('loginstudents')

def studentdataforstudent(request):
    if 'Studentid' in request.session:
        student_id = request.session['Studentid']
        try:
            student = Student.objects.get(Studentid=student_id)
            context = {'student': student}
            return render(request, 'studentdataforstudent.html', context)
        except Student.DoesNotExist:
            return render(request, 'viewachievementforstudent.html')
    else:
        return redirect('loginstudents')

def updatestudent(request, student_id):
    student = get_object_or_404(Student, Studentid=student_id)

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        programme = request.POST['programme']

        student.Studentname = name
        student.Studentphone = phone
        student.Studentprogramme = programme
        student.save()

        return redirect('studentdata')

    context = {
        'student': student,
    }

    return render(request, 'updatestudent.html', context)