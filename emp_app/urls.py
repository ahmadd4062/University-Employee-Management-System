from django.urls import path
from emp_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('home' , views.home , name = "home"),
    path('view_all_emp', views.view_all_emp, name="view_all_emp"),
    path('add_emp', views.add_emp, name="add_emp"),
    path('remove_emp', views.remove_emp, name="remove_app"),
    path('remove_emp/<int:emp_id>', views.remove_emp, name="remove_app"),
    path('filter_emp' , views.filter_emp , name = "filter_emp"),
    path('books', views.books, name="books"),
    path('meeting', views.meeting, name="meeting"),
    path('expenses', views.expenses , name="expenses"),
    path('feedback', views.feedback , name="feedback"),
    path('payroll' , views.payroll , name="payroll"),
    path('training', views.training,name = "training"),
    path('task', views.task, name="task"),
    path('location' , views.location, name = "location"),
    path('images', views.images, name = "images"),
    path('attendance_form', views.create_attendance_view, name='attendance_form'),
    path('show_attendance', views.show_attendance_view, name='show_attendance'),


]