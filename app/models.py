from django.db import models
from django.utils import timezone
def increment_invoice_number():
    last_invoice = Order_Detail.objects.all().order_by('id').last()
    if not last_invoice:
        return 'ORD0001'
    order_id = last_invoice.order_id
    invoice_int = int(order_id.split('ORD')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'ORD' + str(formatted)
    return new_invoice_no  

class Order_Detail(models.Model):
    order_id = models.CharField('Order Id',max_length = 500, default = increment_invoice_number, null = True, blank = True)
    buyer_name = models.CharField('Buyer Name',max_length=100)
    email = models.EmailField('Email Id',max_length=100)
    mobile = models.CharField('Mobile Num',max_length=30)
    order_item = models.CharField('Order Item',max_length=300)
    quantity = models.IntegerField('Quantity')
    image = models.FileField('Product Sample Image',upload_to='product/',null=True)
    ordered_date = models.DateField('Ordered Date')
    delivery_date = models.DateField('Delivery Date')
    amount_per_product = models.CharField('Amount Per Product',max_length=300)
    city = models.CharField('Buyer City',max_length=300)
    address = models.TextField('Buyer Address',max_length=2000)
    notes = models.TextField('Notes',max_length=3000)
    invoice_status = models.CharField('Invoice Status',max_length=300,null=True,blank=True,default='NotSend')
    def __str__(self):
        return self.buyer_name

class Stock(models.Model):
	order_id = models.CharField(max_length=128)
	buyers = models.ManyToManyField(Order_Detail, through='Stock_Detail')
	def __str__(self):
	    return self.order_id
class Stock_Detail(models.Model):
	buyer_name = models.ForeignKey(Order_Detail, on_delete=models.CASCADE)
	stock_name = models.ForeignKey(Stock, on_delete=models.CASCADE)
	item_name = models.CharField(max_length=300)
	no_of_stock = models.CharField(max_length=300)
	def __str__(self):
		return self.item_name
class HRTeam(models.Model):
    hr_name = models.CharField('HR Name',max_length=100)
    email = models.EmailField('Email Id',max_length=100)
    mobile = models.CharField('Mobile Num',max_length=30)
    username = models.CharField('Username',max_length=30)
    password = models.CharField('Password',max_length=30)
    dob = models.DateField()
    doj = models.DateField()
    bio_data = models.FileField('Bio Data',upload_to='documents/',null=True)
    city = models.CharField(' City',max_length=300)
    address = models.TextField(' Address',max_length=2000)
    def __str__(self):
        return self.hr_name
STATUS = (
    ('','Select'),
    ('Knitting','Knitting'),
    ('Dying', 'Dying'),
    ('Cutting','Cutting and Stitching'),
    ('Printing','Printing'),
    ('Ironing','Ironing'),
    ('Quality','Quality Checking and Packing'),
    ('Checking','Checking and Approval'),
)
USER_TYPE = (
    ('','Select'),
    ('Normal','Normal'),
    ('Manager', 'Manager'),
)
STS = (
    ('','Select'),
    ('yettostart','Yet to Start'),
    ('Processing', 'Processing'),
    ('Finish', 'Finish'),
)
PAYMENT = (
    ('','Select'),
    ('rised','Invoice Rised'),
    ('send', 'Email Send'),
    ('paid', 'Payment Received'),
)
class Employee_Detail(models.Model):
    employee_name = models.CharField('Employee Name',max_length=100)
    email = models.EmailField('Email Id',max_length=100)
    mobile = models.CharField('Mobile Num',max_length=30)
    username = models.CharField('Username',max_length=30,unique=True)
    password = models.CharField('Password',max_length=30)
    dob = models.DateField()
    doj = models.DateField()
    bio_data = models.FileField('Bio Data',upload_to='documents/',null=True)
    city = models.CharField(' City',max_length=300)
    address = models.TextField(' Address',max_length=2000)
    per_day = models.CharField('Per Day Salary',max_length=100,null=True)
    department = models.CharField('Department',max_length=300,choices=STATUS)
    user_type  = models.CharField('User Type',max_length=300,choices=USER_TYPE)
    def __str__(self):
        return self.employee_name
class Work_Detail(models.Model):
    order_id = models.CharField('Order Id',max_length=100)
    buyer_name = models.ForeignKey(Order_Detail, on_delete=models.CASCADE)
    material_name = models.CharField('Material Name',max_length=300,null=True)
    total_quantity = models.CharField('Total Quantity',max_length=30)
    final_delivered_Quantity = models.CharField('Final Delivered Quantity',max_length=30,null=True, blank = True)
    delivery_date = models.DateField()
    department = models.CharField('Department',max_length=300,choices=STATUS)
    status =  models.CharField('Staus',max_length=300,choices=STS)
    notes = models.TextField('Notes',max_length=3000,null=True)
    def __str__(self):
        return self.order_id
class Shipping(models.Model):
    order_id = models.CharField('Order Id',max_length=100)
    buyer_name = models.ForeignKey(Order_Detail, on_delete=models.CASCADE)
    material_name = models.CharField('Material Name',max_length=300,null=True)
    total_quantity = models.CharField('Total Quantity',max_length=30) 
    shipped_date = models.DateField()   
    delivered_date = models.DateField()
    mode_of_shippment = models.CharField('Mode of Shipping',max_length=300)
    notes = models.TextField('Notes',max_length=3000,null=True)
    def __str__(self):
        return self.order_id
class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee_Detail,on_delete=models.CASCADE)
    attendance = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    def __str__(self):
        return self.employee_id.employee_name
class Invoice(models.Model):
    buyer_name = models.ForeignKey(Order_Detail,on_delete=models.CASCADE)
    order_id = models.CharField('Order Id',max_length=100)
    due_date = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    notes = models.TextField('Notes',max_length=3000,null=True)
    payment_status =  models.CharField('Payment Status',max_length=300,choices=PAYMENT)
    created_date = models.DateField(default=timezone.now())
    def __str__(self):
        return self.order_id
    def publish(self):
        self.created_date = timezone.now()
        self.save()
OPT = (
    ('','Select'),
    ('Open','Open'),
    ('Closed', 'Closed'),
)
class Job_Detail(models.Model):
    company_name = models.CharField('Company Name',max_length=300)
    job_title = models.CharField('Job Title',max_length=300)
    description = models.CharField('Job Description',max_length=300)
    position = models.CharField('Position',max_length=300)
    experience = models.CharField('Experience',max_length=300)
    area_of_work = models.CharField('Area of Work',max_length=300,choices=STATUS)
    salary = models.CharField('Salary',max_length=300)
    status = models.CharField('Job Status',max_length=30,null=True,choices=OPT)
    def __str__(self):
        return self.company_name
class UserDetail(models.Model):
    name = models.CharField('Name',max_length=100)
    email = models.EmailField('Email Id',max_length=100)
    mobile = models.CharField('Mobile Num',max_length=30)
    username = models.CharField('Username',max_length=30)
    password = models.CharField('Password',max_length=30)
    dob = models.DateField()
    resume = models.FileField('Bio Data',upload_to='documents/',null=True)
    city = models.CharField(' City',max_length=300)
    address = models.TextField(' Address',max_length=2000)
    def __str__(self):
        return self.name
JOB_STATUS = (
    ('','Select'),
    ('pending','Pending'),
    ('Shorlisted','Shorlisted'),
    ('Rejected', 'Rejected'),
    ('Hired', 'Hired'),
)
class Job_Apply(models.Model):
    job_id = models.ForeignKey(Job_Detail, on_delete=models.CASCADE)
    user_name = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    status = models.CharField('Status',max_length=300,null=True,blank=True,choices=JOB_STATUS)
    interview_date = models.DateField('Interview Date',null=True,blank=True)
    time = models.CharField('Interview Time',max_length=30,null=True,blank=True)
    address = models.TextField('Interview Conducting Place',max_length=2000,null=True,blank=True)
    def __str__(self):
        return self.user_name.name


class Expense(models.Model):
    expense_user=models.ForeignKey(HRTeam,on_delete=models.CASCADE)
    expense_name=models.CharField(max_length=100)
    expense_purpose=models.CharField(max_length=500)
    expense_amount=models.BigIntegerField()
    expense_file=models.ImageField(upload_to="Expense")
    expense_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expense_name
    
class Meeting(models.Model):
    meeting_employee=models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    meeting_name=models.CharField(max_length=200)
    meeting_platform=models.CharField(max_length=100)
    meeting_place=models.CharField(max_length=200)
    meeting_date=models.DateTimeField()

    def __str__(self):
        return self.meeting_name
    
class Medical(models.Model):
    medical_employee=models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    medical_policy=models.CharField(max_length=200)
    medical_description=models.CharField(max_length=200)
    medical_amount=models.BigIntegerField()
    def __str__(self):
        return self.medical_policy

class Inventory(models.Model):
    stock_name=models.CharField(max_length=200)
    stock_description=models.CharField(max_length=200)
    stock_quantity=models.CharField(max_length=200)
    stock_damages=models.CharField(max_length=200,default='No Damages')
    def __str__(self):
        return self.stock_name
