from django.shortcuts import render , HttpResponse 
from .models import Employee, Role , Department
from datetime import datetime
from django.db.models import Q
from .models import Book
from .models import Meeting
from .models import Expense
from .models import Feedback
from .models import Payroll
from .models import Training
from .models import Task
from .models import Img
from django.shortcuts import render
from .models import Attendance





# Create your views here.

def home(request):
    return render(request , "home.html")  

def view_all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, "view_all_emp.html" , context)


from django.shortcuts import get_object_or_404

def add_emp(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salaary = int(request.POST['salaary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_id = int(request.POST['dept'])
        role_id = int(request.POST['role'])

        # Retrieve Department and Role instances
        department = get_object_or_404(Department, pk=dept_id)
        role = get_object_or_404(Role, pk=role_id)

        # Create and save the new Employee instance
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salaary=salaary,
            bonus=bonus,
            phone=phone,
            dept=department,
            role=role,
            hire_date=datetime.now()
        )
        new_emp.save()

        return HttpResponse("University Employee Added Successfully")
    elif request.method == 'GET':
        return render(request, "add_emp.html")
    else:
        return HttpResponse("An Exception Occurred, Employee has not been added")




def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter the valid Employee ID")
    emps=Employee.objects.all()
    context = {
            'emps' : emps
        }
    return render(request, "remove_emp.html", context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, "view_all_emp.html", context)
    elif request.method == 'GET':
        return render(request, "filter_emp.html")
    else:
        return HttpResponse("An Exception Occured")




def books(request):
    books = Book.objects.all()
    context={
        'books': books
    }
    return render(request, "books.html", context)



def meeting(request):
    if request.method == 'POST':
        name = request.POST['name']
        description=request.POST['description']
        dept = request.POST['dept']
        
        meeting= Meeting(name=name,description=description,dept=Department,start_time=datetime.now (), end_time=datetime.now ())
        meeting.save()
        return HttpResponse("Meeting Time Set Successfully")
    elif request.method=='GET':
        return render(request,"meeting.html")
    else:
        return HttpResponse('An exception occured, Time has not been set')
    

def expenses(request):
    if request.method == 'POST':
        name = request.POST['name']
        description=request.POST['description']
        amount = request.POST['amount']
        date = request.POST['date']
        
        
        expenses=Expense(name=name , description=description , amount = amount , date=datetime.now())
        expenses.save()
        return HttpResponse("Expense added successfully")
    elif request.method=='GET':
        return render(request,"expenses.html")
    else:
        return HttpResponse('An exception occured, expense has not been added')
    


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email=request.POST['email']
        content = request.POST['content']
    
        feedback= Feedback(name=name , email=email , content=content)
        feedback.save()
        return HttpResponse("Feedback added successfully")
    elif request.method=='GET':
        return render(request,"feedback.html")
    else:
        return HttpResponse('An exception occured, feedback has not been added')
    


def payroll(request):
    if request.method == 'POST':
        name = request.POST['name']
        start_time=request.POST['start_time']
        end_time = request.POST['end_time']
        basic_pay = request.POST['basic_pay']
        overtime_pay = request.POST['overtime_pay']
        tax_deducted = request.POST['tax_deducted']
        netpay = request.POST['netpay']
    
        payroll=Payroll(name=name , start_time=datetime.now(), end_time=datetime.now(), basic_pay=basic_pay , overtime_pay=overtime_pay , tax_deducted=tax_deducted , netpay=netpay)
        payroll.save()
        return HttpResponse("Empoyee Payroll added successfully")
    elif request.method=='GET':
        return render(request, "payroll.html")
    else:
        return HttpResponse('An exception occured, payroll has not been added')
    

    
def training(request):
    if request.method == 'POST':
        name = request.POST['name']
        description=request.POST['description']
        dept = request.POST['dept']
        start_time=request.POST['start_time']
        end_time = request.POST['end_time']

        training=Training( name=name , description=description, dept=dept, start_time=datetime.now(), end_time=datetime.now())
        training.save()
        return HttpResponse("Employee Traning Plan added successfully")
    elif request.method=='GET':
        return render(request, "training.html")
    else:
        return HttpResponse('An exception occured, training has not been added')
    

def task(request):
    if request.method == 'POST':
        name = request.POST['name']
        description=request.POST['description']
        dept = request.POST['dept']
        start_time=request.POST['start_time']
        end_time = request.POST['end_time']

        task=Task( name=name , description=description, dept=dept, start_time=datetime.now(), end_time=datetime.now())
        task.save()
        return HttpResponse("Employee Task added successfully")
    elif request.method=='GET':
        return render(request, "task.html")
    else:
        return HttpResponse('An exception occured, task has not been added')
    

def location(request):
    return render(request, "location.html")


def images(request):
    images = Img.objects.all()
    context={
        'images': images
    }
    return render(request, "images.html", context)



def create_attendance_view(request):
    if request.method == 'POST':
        employee_id = request.POST['employee']
        date = request.POST['date']
        status = request.POST['status']
 
        date = date.today() if not date else date

        new_attendance = Attendance(employee_id=employee_id, date=date, status=status)
        new_attendance.save()

        return HttpResponse("Attendance Created Successfully")
    else:
        employees = Employee.objects.all()
        return render(request, 'attendance_form.html', {'employees': employees})
    
def show_attendance_view(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'show_attendance.html', {'attendance_records': attendance_records})








    



    

    





    



    



