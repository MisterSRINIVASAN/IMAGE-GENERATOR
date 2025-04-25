from django.urls import path
from . import views

urlpatterns = [
	path('rise_invoice/', views.rise_invoice,name="rise_invoice"),
	path('hr_login/', views.hr_login,name="hr_login"),
	path('hr_dashboard/', views.hr_dashboard,name="hr_dashboard"),
	path('logout/', views.logout,name="logout"),
	path('add_employee/', views.add_employee,name="add_employee"),
	path('employee/', views.employee,name="employee"),
	path('edit_employee/<int:pk>/', views.edit_employee,name="edit_employee"),
	path('delete/<int:pk>/', views.delete,name="delete"),
	path('work_details/<int:pk>/', views.work_details,name="work_details"),
	path('buyer_detail/', views.buyer_detail,name="buyer_detail"),
	path('employee_login/', views.employee_login,name="employee_login"),
	path('employee_dashboard/', views.employee_dashboard,name="employee_dashboard"),
	path('employee_logout/', views.employee_logout,name="employee_logout"),
	path('employee_work/', views.employee_work,name="employee_work"),
	path('edit/<int:pk>/', views.edit,name="edit"),
	path('employee_attendance/', views.employee_attendance,name="employee_attendance"),
	path('show_attendance/', views.show_attendance,name="show_attendance"),
	path('render/pdf/', views.gen_pdf,name='gen_pdf'),
	path('invoice/<int:pk>/', views.invoice,name='invoice'),
	path('rised_invoice/', views.rised_invoice,name="rised_invoice"),
	path('employee_salary/', views.employee_salary,name="employee_salary"),
	path('calculate_salary/<int:pk>/', views.calculate_salary,name="calculate_salary"),
	path('add_job/', views.add_job,name="add_job"),
	path('jobs/', views.jobs,name="jobs"),
	path('delete_job/<int:pk>/', views.delete_job,name="delete_job"),
	path('', views.register,name="register"),
	path('user_login/', views.user_login,name="user_login"),
	path('user_dashboard/', views.user_dashboard,name="user_dashboard"),
	path('job_details/', views.job_details,name="job_details"),
	path('apply/<int:pk>/', views.apply,name="apply"),
	path('applied_jobs/', views.applied_jobs,name="applied_jobs"),
	path('applied_candidates/', views.applied_candidates,name="applied_candidates"),
	path('update/<int:pk>/', views.update,name="update"),
	path('location/<int:pk>/', views.location,name="location"),
	path('user_logout/', views.user_logout,name="user_logout"),
    path('add_expense/',views.add_expense,name='add_expense'),
    path('view_expense/',views.view_expense,name='view_expense'),
    path('view_meetings/',views.view_meetings,name='view_meetings'),
    path('view_medical/',views.view_medical,name='view_medical')
	

	
]
