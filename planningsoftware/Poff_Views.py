from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib import messages



def Home(request):
    return render(request,"PlanningOfficer/Home.html")



def ADD_PROJECT(request):
    
    if request.method == "POST":
        fiscal_id = request.POST.get("fiscal")
        fiscal = CurrentFiscalYear.objects.get(id =fiscal_id )
        procurement_type_id = request.POST.get("procurement_type")
        procurement_type = Procurement_Type.objects.get(id =procurement_type_id )
        budget_type_id = request.POST.get("budget_type")
        budget_type = Budget_Type.objects.get(id =budget_type_id )
        ward_id = request.POST.get("ward")
        ward = Ward.objects.get(id=ward_id)
        name = request.POST.get("name")
        address = request.POST.get("address")
        budget = request.POST.get("budget")
       
        project = Project (
            fiscalyear = fiscal,
            name = name,
            ward = ward,
            address = address,
            procurement_type = procurement_type,
            budget_type =budget_type,
            budget = budget,
        )
        project.save()
        messages.success(request,  " Successfully Added !")
        return redirect('add_usercommittee') 

    
    current_fiscalyear = CurrentFiscalYear.objects.all()
    ward = Ward.objects.all()
    procurement_type = Procurement_Type.objects.all()
    budget_type = Budget_Type.objects.all()
    
    context = {
        "current_fiscalyear":current_fiscalyear,
        "ward":ward,
        "procurement_type":procurement_type,
        "budget_type":budget_type
        
        
    }
    
    return render(request,"PlanningOfficer/add_project.html",context)




def PRINT_CONTRACT_DOCUMENT(request):
    return render(request,"PlanningOfficer/contract_paper.html")
