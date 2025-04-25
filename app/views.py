from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
import datetime
from django.db.models import Q
from django.db import connection
import random 
from django.db.models import Sum, Count
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils import timezone
from .render import Render
from django.template.loader import get_template
from django.http import HttpResponse
def hr_login(request):
	if request.session.has_key('hr'):
		return redirect("add_job")
	else:
		if request.method == 'POST':
			username = request.POST.get('uname')
			password =  request.POST.get('psw')
			post = HRTeam.objects.filter(username=username,password=password)
			if post:
				username = request.POST.get('uname')
				request.session['hr'] = username
				a = request.session['hr']
				sess = HRTeam.objects.only('id').get(username=a).id
				request.session['hr_id']=sess
				return redirect("add_job")
			else:
				messages.success(request, 'Invalid Username or Password')
	return render(request,'hr_login.html',{})
def hr_dashboard(request):
	if request.session.has_key('hr'):
		return render(request,'hr_dashboard.html',{})
	else:
		return render(request,'hr_login.html',{})
def logout(request):
    try:
        del request.session['hr']
    except:
     pass
    return render(request, 'hr_login.html', {})
def add_employee(request):
	if request.method == 'POST':
		employee_name = request.POST.get('employee_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		dob = request.POST.get('dob')
		doj = request.POST.get('doj')
		department = request.POST.get('department')
		user_type = request.POST.get('user_type')
		city = request.POST.get('city')
		bio_data = request.FILES['bio_data']
		address = request.POST.get('address')
		salary = request.POST.get('salary')
		crt = Employee_Detail.objects.create(employee_name=employee_name,username=username,
		password=password,email=email,mobile=mobile,dob=dob,per_day=salary,
		doj=doj,department=department,user_type=user_type,bio_data=bio_data,city=city,
		address=address)
		if crt:
			messages.success(request,'Employee Added Successfully')
	return render(request,'add_employee.html',{})
def employee(request):
	if request.session.has_key('hr'):
		detail = Employee_Detail.objects.all()
		return render(request,'employee.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})
	
def view_expense(request):
	if request.session.has_key('hr'):
		detail = Expense.objects.all()
		return render(request,'view_expense.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})

def edit_employee(request,pk):
	detail = Employee_Detail.objects.filter(id=pk)
	if request.method == 'POST':
		employee_name = request.POST.get('employee_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		department = request.POST.get('department')
		user_type = request.POST.get('user_type')
		city = request.POST.get('city')
		address = request.POST.get('address')
		per_day = request.POST.get('salary')
		crt = Employee_Detail.objects.filter(id=pk).update(employee_name=employee_name,username=username,email=email,mobile=mobile,department=department,user_type=user_type,city=city,
		address=address,per_day=per_day)
		if crt:
			messages.success(request,'Employee Updated Successfully')
	return render(request,'edit_employee.html',{'detail':detail})
def delete(request,pk):
	if request.session.has_key('hr'):
		detail = Employee_Detail.objects.filter(id=pk).delete()
		return redirect('employee')
	else:
		return render(request,'hr_login.html',{})
def work_details(request,pk):
	if request.session.has_key('hr'):
		detail = Work_Detail.objects.filter(id=pk)
		return render(request,'work_details.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})
def buyer_detail(request):
	if request.session.has_key('hr'):
		detail = Order_Detail.objects.all()
		return render(request,'buyer_detail.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})
def employee_login(request):
	if request.session.has_key('employee'):
		return redirect("employee_work")
	else:
		if request.method == 'POST':
			username = request.POST.get('uname')
			password =  request.POST.get('psw')
			user_type = request.POST.get('department')
			post = Employee_Detail.objects.filter(username=username,password=password,department=user_type,user_type='Manager')
			if post:
				username = request.POST.get('uname')
				request.session['employee'] = username
				request.session['department'] = user_type
				a = request.session['employee']
				sess = Employee_Detail.objects.only('id').get(username=a).id
				request.session['employee_id']=sess
				return redirect("employee_work")
			else:
				messages.success(request, 'Invalid Username or Password')
	return render(request,'employee_login.html',{})
def employee_dashboard(request):
	if request.session.has_key('employee'):
		return render(request,'employee_dashboard.html',{})
	else:
		return render(request,'employee_login.html',{})
def employee_logout(request):
    try:
        del request.session['employee']
    except:
     pass
    return render(request, 'employee_login.html', {})
def employee_work(request):
	if request.session.has_key('employee'):
		dept = request.session['department']
		detail = Work_Detail.objects.filter(department=dept)
		return render(request,'employee_work.html',{'detail':detail})
	else:
		return render(request,'employee_login.html',{})
def edit(request,pk):
	if request.session.has_key('employee'):
		dept = request.session['department']
		detail = Work_Detail.objects.filter(department=dept,id=pk)
		if request.method == 'POST':
			final_delivered_Quantity = request.POST.get('final_delivered_Quantity')
			status = request.POST.get('status')
			crt = Work_Detail.objects.filter(department=dept,id=pk).update(final_delivered_Quantity=final_delivered_Quantity,status=status)
			if crt:
				return redirect('employee_work')
		return render(request,'edit.html',{'detail':detail})
	else:
		return render(request,'employee_login.html',{})
def employee_attendance(request):
    if request.session.has_key('hr'):
        return render(request,'employee_attendance.html',{})
    else:
        return redirect("hr_login")
def show_attendance(request):
    if request.session.has_key('hr'):
        date = request.GET.get('date')
        detail = Employee_Detail.objects.all()
        if request.method == 'POST':
            student_id = request.POST.getlist('emp_id[]')
            attendance = request.POST.getlist('attendance[]')
            date = request.POST.get('date')
            month = request.POST.get('month')
            length=len(student_id)
            for row in range(0,length):
                s_id =  Employee_Detail.objects.get(id=int(student_id[row]))
                ad = Attendance.objects.create(employee_id=s_id,month=month,
                date=date,attendance=attendance[row])
                if ad:
                    messages.success(request,'Added')
        att = Attendance.objects.filter(date=date)
        tot = Attendance.objects.filter(date=date).aggregate(Count('employee_id'))
        present = Attendance.objects.filter(date=date,attendance='yes').aggregate(Count('attendance'))
        absent = Attendance.objects.filter(date=date,attendance='no').aggregate(Count('attendance'))
        return render(request,'show_attendance.html',{'detail':detail,'att':att,'tot':tot,'present':present,'absent':absent})
    else:
        return redirect("hr_login")
from django.contrib.auth.decorators import login_required
@login_required
def rise_invoice(request):
	detail = Order_Detail.objects.filter(invoice_status='NotSend')
	return render(request,'rise_invoice.html',{'detail':detail})
def gen_pdf(request):
    ids = request.GET.get('order_id')
    order_ids = request.GET.get('id')
    sales = Order_Detail.objects.filter(order_id=ids,id=int(order_ids))
    invoice = Invoice.objects.filter(order_id=ids,buyer_name=int(order_ids))
    today = timezone.now()
    params = {
        'today': today,
        'sales': sales,
        'request': request,
        'invoice':invoice
    }
    return Render.render('pdf.html', params)
@login_required
def invoice(request,pk):
	detail = Order_Detail.objects.filter(id=pk)
	ids = Order_Detail.objects.get(id=pk)
	if request.method == 'POST':
		order_id = request.POST.get('order_id')
		amount = request.POST.get('amount')
		due_date = request.POST.get('due_date')
		notes = request.POST.get('notes')
		crt = Invoice.objects.create(order_id=order_id,amount=amount,due_date=due_date,
		notes=notes,payment_status='rised',buyer_name=ids)
		if crt:
			return redirect('rised_invoice')
	return render(request,'invoice.html',{'detail':detail})
@login_required
def rised_invoice(request):
	detail = Invoice.objects.filter(payment_status='rised')
	return render(request,'rised_invoice.html',{'detail':detail})
def email(request):
    if request.method == "POST":
        form = EmailForm(request.POST,request.FILES)
        if form.is_valid():
            cid = request.GET.get('cid')
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.clientname = int(cid)
            post.projectid = int(request.GET.get('pid'))
            post.invoiceid = int(request.GET.get('iid'))
            post.status ='send'
            post.save()
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            document = request.FILES.get('document')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            bcc_email = settings.EMAIL_HOST_USER
            email = EmailMessage(subject,message,email_from,recipient_list,bcc=[bcc_email])
            base_dir = 'media/documents/'
            email.attach_file('media/documents/'+str(document))
            email.send()
            invoiceid = request.GET.get('iid')
            date = datetime.now()
            Invoice.objects.filter(pk=int(invoiceid)).update(status='send',mail_send_date=date)
            return redirect('payment_pending')
    else:
        form = EmailForm()
    return render(request, 'billing/email_form.html', {'form': form})

def employee_salary(request):
	if request.session.has_key('hr'):
		detail = Employee_Detail.objects.all()
		return render(request,'employee_salary.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})

def calculate_salary(request,pk):
	if request.session.has_key('hr'):
		if request.method == 'GET':
			from_date = request.GET.get('from')
			to_date = request.GET.get('to')
			extra = request.GET.get('extra')
			cursor = connection.cursor()
			sql_user = ''' SELECT COUNT(app_attendance.attendance) from app_attendance 
			where app_attendance.employee_id_id='%d' AND app_attendance.attendance='yes' AND app_attendance.date BETWEEN '%s' AND '%s'
			''' %(pk,from_date,to_date)
			post_user = cursor.execute(sql_user)
			row_user = cursor.fetchall()
			detail = Employee_Detail.objects.filter(id=pk)
			return render(request,'calculate_salary.html',{'detail':detail,'row_user':row_user})
		return render(request,'calculate_salary.html',{})
	else:
		return render(request,'hr_login.html',{})
def add_expense(request):
	if request.session.has_key('hr'):
		hr=request.session['hr_id']
		hr_id=HRTeam.objects.get(id=int(hr))
		if request.method == 'POST':
			expense_name=request.POST.get('expense_name')
			expense_purpose=request.POST.get('expense_purpose')
			expense_amount=request.POST.get('expense_amount')
			expense_file=request.FILES['expense_file']
			row=Expense.objects.create(expense_user=hr_id,expense_name=expense_name,expense_purpose=expense_purpose,
							  expense_amount=expense_amount,expense_file=expense_file)
			if row:
				messages.success(request,'Expense Added Successfully!')
				return redirect('add_expense')
			else:
				messages.error(request,'Error!')
	
	return render(request,'add_expense.html')
def add_job(request):
	if request.session.has_key('hr'):
		if request.method == 'POST':
			job_title = request.POST.get('job_title')
			position = request.POST.get('position')
			experience = request.POST.get('experience')
			salary = request.POST.get('salary')
			area_of_work = request.POST.get('area_of_work')
			description = request.POST.get('description')
			company_name = request.POST.get('company_name')
			status = request.POST.get('status')
			crt = Job_Detail.objects.create(company_name=company_name,job_title=job_title,position=position,
			experience=experience,salary=salary,area_of_work=area_of_work,description=description,status=status)
			if crt:
				messages.success(request,'Job Added Successfully')
		return render(request,'add_job.html',{})
	else:
		return render(request,'hr_login.html',{})
def jobs(request):
	if request.session.has_key('hr'):
		detail = Job_Detail.objects.all()
		return render(request,'jobs.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})
def delete_job(request,pk):
	if request.session.has_key('hr'):
		detail = Job_Detail.objects.filter(id=pk).delete()
		return redirect('jobs')
	else:
		return render(request,'hr_login.html',{})
def register(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		dob = request.POST.get('dob')
		city = request.POST.get('city')
		resume = request.FILES['resume']
		address = request.POST.get('address')
		user_exist = UserDetail.objects.filter(username=username)
		if user_exist:
			messages.success(request,'Username Already Exist')
		else:
			crt = UserDetail.objects.create(name=name,username=username,
			password=password,email=email,mobile=mobile,dob=dob,resume=resume,city=city,
			address=address)
			if crt:
				messages.success(request,'Registered Successfully')
	return render(request,'register.html',{})
def user_login(request):
	if request.session.has_key('user'):
		return redirect("user_dashboard")
	else:
		if request.method == 'POST':
			username = request.POST.get('uname')
			password =  request.POST.get('psw')
			post = UserDetail.objects.filter(username=username,password=password)
			if post:
				username = request.POST.get('uname')
				request.session['user'] = username
				a = request.session['user']
				sess = UserDetail.objects.only('id').get(username=a).id
				request.session['user_ids']=sess
				return redirect("user_dashboard")
			else:
				messages.success(request, 'Invalid Username or Password')
	return render(request,'user_login.html',{})
def user_dashboard(request):
	if request.session.has_key('user'):
		return render(request,'user_dashboard.html',{})
	else:
		return render(request,'user_login.html',{})
def job_details(request):
	if request.session.has_key('user'):
		detail = Job_Detail.objects.filter(status='Open')
		return render(request,'job_details.html',{'detail':detail})
	else:
		return render(request,'user_login.html',{})
def apply(request,pk):
	if request.session.has_key('user'):
		user_id = request.session['user_ids']
		job_id = Job_Detail.objects.get(id=pk)
		detail = UserDetail.objects.get(id=int(user_id))
		Job_Apply.objects.create(job_id=job_id,user_name=detail,status='pending')
		return render(request,'apply.html',{})
	else:
		return render(request,'user_login.html',{})
def applied_jobs(request):
	if request.session.has_key('user'):
		user_id = request.session['user_ids']
		detail=Job_Apply.objects.filter(user_name=int(user_id))
		return render(request,'applied_jobs.html',{'detail':detail})
	else:
		return render(request,'user_login.html',{})
	
def view_meetings(request):
	if request.session.has_key('user'):
		user_id = request.session['user_ids']
		detail=Meeting.objects.filter(meeting_employee=int(user_id))
	return render(request,'view_meetings.html',{'detail':detail})

def view_medical(request):
	if request.session.has_key('user'):
		user_id = request.session['user_ids']
		detail=Medical.objects.filter(medical_employee=int(user_id))
	return render(request,'view_medical.html',{'detail':detail})

def applied_candidates(request):
	if request.session.has_key('hr'):
		detail=Job_Apply.objects.all()
		return render(request,'applied_candidates.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})
def update(request,pk):
	if request.session.has_key('hr'):
		detail = Job_Apply.objects.filter(id=pk)
		if request.method == 'POST':
			status = request.POST.get('status')
			interview_date = request.POST.get('interview_date')
			time = request.POST.get('time')
			address = request.POST.get('address')
			upd=Job_Apply.objects.filter(id=pk).update(interview_date=interview_date,status=status,
			time=time,address=address)
			if upd:
				return redirect('applied_candidates')
		return render(request,'update.html',{'detail':detail})
	else:
		return render(request,'hr_login.html',{})
def location(request,pk):
	if request.session.has_key('user'):
		detail=Job_Apply.objects.filter(id=pk)
		return render(request,'location.html',{'detail':detail})
	else:
		return render(request,'user_login.html',{})

def user_logout(request):
    try:
        del request.session['user']
    except:
     pass
    return render(request, 'user_login.html', {})