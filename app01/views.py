from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')

    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/list")


def depart_delete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()

    return redirect("/depart/list")


def depart_edit(request, nid):
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"row_object": row_object})

    title = request.POST.get("title")

    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")


def user_list(request):
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {"queryset": queryset})


def user_add(request):
    if request.method == 'GET':
        context = {
            "gender_choices": models.UserInfo.gender_choices,
            "depart_list": models.Department.objects.all()
        }
        return render(request, "user_add.html", context)

    user= request.POST.get('user')
    pwd= request.POST.get('pwd')
    age= request.POST.get('age')
    account= request.POST.get('ac')
    ctime= request.POST.get('ctime')
    gender= request.POST.get('gd')
    depart_id= request.POST.get('dp')

    models.UserInfo.objects.create(name=user, password=pwd, age= age,account=account,create_time=ctime,gender=gender,depart_id=depart_id)
    return redirect("/user/list/")