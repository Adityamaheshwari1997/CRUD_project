from django.shortcuts import render
from employee.models import Employee


# Create your views here.
def home(request):
    query_set = Employee.objects.all()
    data = {'row': query_set}

    if data is not None:
        return render(request, "index.html", data)
    else:
        return render(request, "empty_msg.html")

def add_member(request):
    return render(request,"add.html")

def insert(request):
    id = request.POST['id_n']
    name = request.POST['name_n']
    mail = request.POST['mail_n']
    mobile = request.POST['Mobile_name']

    emp = Employee(eid = id , ename = name , mail = mail , emobile = mobile)
    emp.save()

    query_set = Employee.objects.all()
    data = {'row': query_set}

    return render(request, "index.html", data)

def delete(request):
    id = request.POST['id']
    e = Employee.objects.filter(eid = id)
    e.delete()
    query_set = Employee.objects.all()
    data = {'row': query_set}
    return render(request,"index.html",data)


def update(request):
    id = request.GET['id']
    query_set = Employee.objects.get(eid = id)
    d = {"data":query_set}
    return render(request,"update.html",d)


def updaterecord(request):
    id = request.POST['id_n']
    name = request.POST['name_n']
    mail = request.POST['mail_n']
    mobile = request.POST['Mobile_name']

    query_set = Employee.objects.get(eid = id)

    if name is not None:
        query_set.ename = name
    if mail is not None:
        query_set.mail = mail
    if mobile is not None:
        query_set.emobile = mobile
    query_set.save()

    query_set = Employee.objects.all()
    data = {'row': query_set}
    return render(request, "index.html", data)
