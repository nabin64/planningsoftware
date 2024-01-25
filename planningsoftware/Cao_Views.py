from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib import messages



def Home(request):
     return render(request, "Cao/Home.html",)
 
def ADD_ACCOUNTANT(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_accountant')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_accountant')
        else:
            user = CustomUser(
                username=username,
                first_name=name,
                email=email,
                user_type=3,
            )
            user.set_password(password)
            user.save()
            accountant = Accountant (
                admin = user,
                name = name,
                mobile = contact,
            )
            accountant.save()
            messages.success(request, user.first_name + "  " +
                             "is Successfully Added !")
            return redirect('view_accountant') 


    return render(request,"Cao/add_accountant.html")



 
 
def ADD_ENGINEER(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_engineer')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_engineer')
        else:
            user = CustomUser(
                username=username,
                first_name=name,
                email=email,
                user_type=4,
            )
            user.set_password(password)
            user.save()
            engineer = Engineer (
                admin = user,
                name = name,
                mobile = contact,
            )
            engineer.save()
            messages.success(request, user.first_name + "  " +
                             "is Successfully Added !")
            return redirect('view_engineer') 
        
    return render(request,"Cao/add_engineer.html")





def ADD_SUBENGINEER(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        ward_ids = request.POST.getlist('wards')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_subengineer')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_subengineer')
        else:
            user = CustomUser(
                username=username,
                first_name=name,
                email=email,
                user_type=5,
            )
            user.set_password(password)
            user.save()
            sub_engineer = SubEngineer (
                admin = user,
                name = name,
                mobile = contact,
            )
            sub_engineer.save()
            sub_engineer.wards.set(ward_ids)
            messages.success(request, user.first_name + "  " +
                             "is Successfully Added !")
            return redirect('view_subengineer')
    wards = Ward.objects.all()
    context = {
        "wards":wards,
       
    } 
    return render(request,"Cao/add_subengineer.html",context)


def ADD_PLANNINGOFFICER(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_engineer')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_planningofficer')
        else:
            user = CustomUser(
                username=username,
                first_name=name,
                email=email,
                user_type=6,
            )
            user.set_password(password)
            user.save()
            planningofficer = PlanningOfficer (
                admin = user,
                name = name,
                mobile = contact,
            )
            planningofficer.save()
            messages.success(request, user.first_name + "  " +
                             "is Successfully Added !")
            return redirect('view_planningofficer') 
    return render(request,"Cao/add_planningofficer.html")


def ADD_WADASACHIB(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        ward_ids = request.POST.getlist('wards')
        print(ward_ids)
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_wadasachib')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_wadasachib')
        else:
            user = CustomUser(
                username=username,
                first_name=name,
                email=email,
                user_type=7,
            )
            user.set_password(password)
            user.save()
            wadasachib = Wadasachib (
                admin = user,
                name = name,
                mobile = contact,
            )
            wadasachib.save()
            wadasachib.wards.set(ward_ids)
            messages.success(request, user.first_name + "  " +
                             "is Successfully Added !")
            return redirect('add_wadasachib')
    wards = Ward.objects.all()
    context = {
        "wards":wards,
       
    }    
    
    return render(request,"Cao/add_wadasachib.html",context)



def VIEW_ACCOUNTANT(request):
    accountant = Accountant.objects.all()
    context = {
        "accountant": accountant
    }
    return render(request,"Cao/view_accountant.html",context)




def VIEW_ENGINEER(request):
    engineer  = Engineer.objects.all()
    context = {
        "engineer":engineer
    }
    return render(request,"Cao/view_engineer.html",context)



def VIEW_SUBENGINEER(request):
    subengineer = SubEngineer.objects.all()
    context = {
        "subengineer" : subengineer
    }
    
    return render(request,"Cao/view_subengineer.html",context)



def VIEW_PLANNINGOFFICER(request):
    planningofficer = PlanningOfficer.objects.all()
    context  = {
        "planningofficer": planningofficer
    }
    return render(request,"Cao/view_planningofficer.html",context)




def VIEW_WADASACHIB(request):
    wadasachib = Wadasachib.objects.all()
    context = {
        "wadasachib":wadasachib
    }
    return render(request,"Cao/view_wadasachib.html",context)