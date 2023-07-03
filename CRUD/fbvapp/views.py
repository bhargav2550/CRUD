from django.shortcuts import render,redirect
from fbvapp.models import student
from fbvapp.forms import studentForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
@login_required
def getstudents(request):
    students=student.objects.all()
    return render(request,"fbvapp/index.html",{"students":students})
@login_required
def createstudent(request):
    form = studentForm()
    if request.method=="POST":
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,"fbvapp/create.html",{"form":form})
@login_required
@permission_required("fbvapp.delete_student")
def deletestudent(request,id):
    students=student.objects.get(id=id)
    students.delete()
    return redirect('/')
@login_required
def updatestudent(request,id):
    students=student.objects.get(id=id)
    form=studentForm(instance=students)
    if request.method=="POST":
        form = studentForm(request.POST,id,instance=students)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"fbvapp/update.html",{"form":form})

def logout(request):
    return render(request,"fbvapp/logout.html")
