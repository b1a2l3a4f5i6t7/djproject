from django.shortcuts import render
from fapp.models import student
from fapp.forms import StudentModelForm
from fapp.models import Teacher
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas

# Create your views here.
@login_required
def homepage(request):
	return render(request,'index.html')
@login_required
@permission_required('fapp. addadmission_student')
def addadmission(request):
    form=StudentModelForm
    studentform= {'form':form}
    if request.method=="POST":
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'fapp/addadmition.html',studentform)
@login_required
@permission_required('fapp.view_student')


def admissionreport(request):
    result=student.objects.all();
    students={ 'allstudents':result}
    return render(request,'fapp/admissionreport.html',students)
@login_required
@permission_required('fapp.delete_student')

def delstudent(request,id):
	s=student.objects.get(id=id)
	s.delete()
	return admissionreport(request)
@login_required
@permission_required('fapp.change_student')

def updatestudent(request,id):
	s=student.objects.get(id=id)
	form=StudentModelForm(instance=s)
	dict={ 'form':form}
	if request.method== "POST":
		form=StudentModelForm(request.POST,instance=s)
		if form.is_valid():
			form.save()
	return render(request, 'fapp/updatefapp.html',dict)
class Teacherread(ListView):
	model=Teacher  
class Teacherdetail(DetailView):
	model=Teacher 	#Teacherdetail data stores in that name
class Insertteacher(CreateView):
	model=Teacher #form=TeacherModelForm
	fields=( 'name','exp','subject','contact') #teacher_form.html
class Updateteacher(UpdateView):
	model=Teacher 
	fields=( 'name','contact') 
@login_required
def homepage(request):
	return render(request,'index.html')
def logoutuser(request):
	return render(request,'logout.html')
def setcookie(request):
	response = HttpResponse("Cookie Set")
	response.set_cookie('working', 'MNC')
	return response
def getcookie(request):
	data=request.COOKIES['working']
	return HttpResponse("Working at:"+data);

def setsession(request):
	request.session['sname'] ='abc'
	request.session['semail'] ='abc@gmail.com'
	return HttpResponse("session is set")
def getsession(request):
	studentname = request.session['sname']
	studentemail = request.session['semail']
	return HttpResponse(studentname+" "+studentemail);
def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="file.csv"'
	writer = csv.writer(response)
	writer.writerow(['10', 'sam','chennai', 'Developer'])
	writer.writerow(['11', 'arun', 'delhi','Tester'])
	return response
def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="file.csv"'
	students = student.objects.all()
	writer = csv.writer(response)
	for s in students:writer.writerow([s.id,s.name,s.fathername,s.classname,s.contact])
	return response
def getpdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="file.pdf"'
	p = canvas.Canvas(response)
	p.setFont("Times-Roman", 55)
	p.drawString(100,700,"Hello, Django.")
	p.showPage()
	p.save()
	return response
