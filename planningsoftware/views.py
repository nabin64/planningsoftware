from django.shortcuts import render, redirect, HttpResponse
from accounts.EmailBackEnd import EmailBackEnd
from accounts.models import *
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


def LOGIN(request):
    return render(request, 'login.html')


def doLogout(request):
    logout(request)
    return redirect('login')
    


@csrf_protect
def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        
        print(user,user.email)

        if user is not None:
            user_type = user.user_type
            if user_type == '1':
                login(request, user)
                return redirect('cao_home')
            elif user_type == "6":
                login(request, user)
                return redirect('poff_home')
            
            else:
                messages.error(request, "Email and Password are Invalids")
                return redirect('login')
        
        messages.error(request, "Email and Password are Invalid")
        return redirect('login')

    return HttpResponseForbidden("Forbidden")



def VIEW_PROJECTS(request):
    projects = Project.objects.all()
    
    context = {
        "projects": projects
    }
    
    return render(request,"Open/view_projects.html",context)



import xlsxwriter
from django.http import HttpResponse


def export_projects_to_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="projects.xlsx"'

    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    headers = [
        'SN',
        'Fiscalyear',
        'Name',
        'Ward',
        'Address',
        'Budget',
        'Budget_type',
        'Sector',
        'Procurement_type',
    ]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    projects = Project.objects.all()
    for row_num, project in enumerate(projects, start=1):
        row = [
            row_num,
            str(project.fiscalyear.fiscal_year) if project.fiscalyear else '',  # Convert FiscalYear to a string
            project.name,
            project.ward.name,
            project.address,
            project.budget,
            str(project.budget_type) if project.budget_type else '',  # Convert BudgetType to a string
            str(project.sector) if project.sector else '',  # Convert Sector to a string
            str(project.procurement_type) if project.procurement_type else '',  # Convert ProcurementType to a string
        ]
        for col_num, cell_value in enumerate(row):
            worksheet.write(row_num, col_num, cell_value)

    workbook.close()
    return response


import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from accounts.forms import ExcelImportForm

# accounts/views.py
import pandas as pd
from django.shortcuts import render, redirect
from accounts.forms import ExcelImportForm
from django.contrib import messages

def import_excel(request):
    if request.method == 'POST' and 'excel_file' in request.FILES:
        excel_file = request.FILES['excel_file']

        try:
            # Read Excel file into a DataFrame
            df = pd.read_excel(excel_file)

            # Drop the 'Fiscalyear' column if it exists
            if 'Fiscalyear' in df.columns:
                df = df.drop('Fiscalyear', axis=1)

            # Ensure that the column names match exactly
            expected_columns = ['Name', 'Ward', 'Address', 'Budget', 'Budget_type', 'Sector', 'Procurement_type']
            if set(df.columns) != set(expected_columns):
                raise ValueError(f"Invalid columns. Expected {expected_columns}, but got {df.columns}")

            # Fetch the latest fiscal year from the database
            latest_fiscal_year = CurrentFiscalYear.objects.latest('fiscal_year')

            # Loop through rows and create Project objects
            for index, row in df.iterrows():
                # Retrieve or create a Ward instance based on the ward name
                ward_instance, created = Ward.objects.get_or_create(name=row['Ward'])

                # Retrieve or create a Project_Sector instance based on the sector name
                sector_instance, created = Project_Sector.objects.get_or_create(name=row['Sector'])

                # Retrieve or create a Procurement_Type instance based on the procurement type name
                procurement_type_instance, created = Procurement_Type.objects.get_or_create(name=row['Procurement_type'])

                # Retrieve or create a Budget_Type instance based on the budget type name
                budget_type_instance, created = Budget_Type.objects.get_or_create(name=row['Budget_type'])

                Project.objects.create(
                    fiscalyear=latest_fiscal_year,
                    name=row['Name'],
                    ward=ward_instance,
                    address=row['Address'],
                    budget=row['Budget'],
                    budget_type=budget_type_instance,
                    sector=sector_instance,
                    procurement_type=procurement_type_instance,
                )

            messages.success(request, 'Data imported successfully')

        except Exception as e:
            messages.error(request, f'Error importing data: {str(e)}')

    else:
        messages.error(request, 'No file uploaded.')

    return render(request, 'Open/import_excel.html')
from datetime import datetime


def ADD_USERCOMMITTEE(request):
    
    if request.method == "POST":
        project_id = request.POST.get("project")
        project = Project.objects.get(id =project_id)
        name = request.POST.get("name")
        formation_date_str = request.POST.get("formation_date")
        chairman_name = request.POST.get("chairman_name")
        chairman_citizenship = request.POST.get("chairman_citizenship")
        chairman_mobile = request.POST.get("chairman_mobile")
        secretary_name = request.POST.get("secretary_name")
        secretary_citizenship = request.POST.get("secretary_citizenship")
        secretary_mobile = request.POST.get("secretary_mobile")
        treasurer_name = request.POST.get("treasurer_name")
        treasurer_citizenship = request.POST.get("treasurer_citizenship")
        treasurer_mobile = request.POST.get("treasurer_mobile")
        member1 = request.POST.get("member1")
        member2 = request.POST.get("member2")
        member3 = request.POST.get("member3")
        member4 = request.POST.get("member4")
        start_date = request.POST.get("start_date")
        accomplish_date = request.POST.get("accomplish_date")
        if formation_date_str:
            # Parse the formation_date string manually
            try:
                formation_date_parsed = datetime.strptime(formation_date_str, '%Y-%m-%d').date()
            except ValueError:
                formation_date_parsed = None
        else:
            formation_date_parsed = None

      
        usercommittee = UserCommitte (
            project = project,
            name = name,
            chairman_name= chairman_name,
            chairman_citizenship=chairman_citizenship,
            chairman_mobile = chairman_mobile,
            secretary_name = secretary_name,
            secretary_citizenship = secretary_citizenship,
            secretary_mobile = secretary_mobile,
            treasurer_name=treasurer_name,
            treasurer_citizenship =treasurer_citizenship,
            treasurer_mobile = treasurer_mobile,
            member1=member1,
            member2=member2,
            member3=member3,
            member4=member4,
            formation_date =formation_date_parsed
        )
        usercommittee.save()
        project.status = 1
        project.start_date = start_date
        project.accomplish_date = accomplish_date
        project.save()
        messages.success(request,  " Successfully Added !")
        
        return redirect('add_cost_estimate')

        
    
    projects = Project.objects.filter(status=0)
    context = {
        "projects":projects
    }
    return render(request,"Open/add_usercommittee.html",context)




def VIEW_USERCOMMITTEE(request):
    usercommittee = UserCommitte.objects.all()
    context = {
        "usercommittee":usercommittee
    }
    return render(request,"Open/view_usercommittee.html",context)



def ADD_CONTRACT(request):
    
    projects = Project.objects.filter(status=1)
    user_committe = UserCommitte.objects.all()
    coste_estimate = Cost_Estimate.objects.all()
    context = {
        "projects":projects,
        "user_committe":user_committe,
        "coste_estimate":coste_estimate
    }
    
    return render(request,"Open/add_contract.html",context)



def ADD_COST_ESTIMATE(request):
    if request.method == "POST":
        project_id = request.POST.get("project")
        project = Project.objects.get(id =project_id)
        budget =request.POST.get("budget")
        congtingency =request.POST.get("congtingency")
        usercontribution =request.POST.get("usercontribution")
        totalcost =request.POST.get("totalcost") 
        cost_estimate = Cost_Estimate (
            project= project,
            budget = budget,
            contigency_amount = congtingency,
            user_contribution = usercontribution,
            cost_estimate = totalcost,

            
        )
        
        cost_estimate.save()
        project.status = 2
        project.save()
        messages.success(request,  " Successfully Added !")
        return redirect('view_estimated_project') 
        
    
    projects = Project.objects.filter(status='1')
    context = {
        "projects":projects,
    }

    return render(request,"Engineer/CostEstimate.html",context)



def VIEW_COST_ESTIMATE(request):
    cost_estimate = Cost_Estimate.objects.all()
    context = {
        "cost_estimate":cost_estimate
    }
    return render(request,"Open/view_cost_estimate.html",context)


from django.shortcuts import render, get_object_or_404
def VIEW_PHOTO_COST_ESTIMATE(request,id):
    cost_estimate = get_object_or_404(Cost_Estimate, id=id)
    print(cost_estimate)
    context = {
        "cost_estimate":cost_estimate
    }
    return render(request,"Open/view_photo_cost_estimate.html",context)



def LOAD_USER_COMMITTEE(request):
    project_id = request.GET.get('projectid')
    usercommittee = UserCommitte.objects.filter(project_id=project_id)
    
    context = {
        "usercommittee":usercommittee
    }
    return render(request,'Ajax/usercommittee_dropdown.html',context)



def LOAD_COST_COMMITTEE(request):
    project_id = request.GET.get('projectid')
    cost_estimate = Cost_Estimate.objects.filter(project_id=project_id)
    context ={
        "cost_estimate" : cost_estimate
    }
    return render(request,'Ajax/cost_estimate_dropdown.html',context)



def LOAD_BUDGET(request):
    project_id = request.GET.get('projectid')
    cost_estimate = Cost_Estimate.objects.filter(project_id=project_id)
    context = {
        "cost_estimate":cost_estimate
    }
    
    return render(request,"Ajax/budget_dropdown.html",context)




def LOAD_CONTINGENCY(request):
    project_id = request.GET.get('projectid')
    cost_estimate = Cost_Estimate.objects.filter(project_id=project_id)
    context = {
        "cost_estimate":cost_estimate
    }
    
    return render(request,"Ajax/contingency_dropdown.html",context)
    
    
    
def LOAD_USER_CONTRIBUTION(request):
    project_id = request.GET.get('projectid')
    cost_estimate = Cost_Estimate.objects.filter(project_id=project_id)
    context = {
        "cost_estimate":cost_estimate
    }
    
    return render(request,"Ajax/user_contribution_dropdown.html",context)



def PRINT_CONTRACT_DOCUMENT(request,id):
    project = Project.objects.get(id = id)
    usercommittee = UserCommitte.objects.get(project_id = id)
    cost_estimate = Cost_Estimate.objects.get(project_id = id)
    office = cost_estimate.budget-cost_estimate.contigency_amount
    
    
    context = {
        "project":project,
        "usercommittee":usercommittee,
        "cost_estimate" :cost_estimate,
        "office":office,
    }
    return render(request,"PlanningOfficer/contract_paper.html",context)




def VIEW_ESTIMATED_PROJECT(request):
    project = Project.objects.filter(status = '2')

    context = {
        "project":project
    }
    
    return render(request,"Open/view_estimated_project.html",context)



def PRINT_TIPPANI(request,id):
    project = Project.objects.get(id = id)
    usercommittee = UserCommitte.objects.get(project_id = id)
    
    context = {
        "project":project,
        "usercommittee":usercommittee
    }
    
    return render(request,"Open/add_tippani.html",context)



def PRINT_BANK_LETTER(request,id):
    project = Project.objects.get(id = id)
    usercommittee = UserCommitte.objects.get(project_id = id)
    cost_estimate = Cost_Estimate.objects.get(project_id=id)
    
    context = {
        "project":project,
        "usercommittee":usercommittee,
        "cost_estimate":cost_estimate
    }
    
    return render(request,"Open/add_bank_letter.html",context)
    
    
def PRINT_WORK_ORDER(request,id):
    project = Project.objects.get(id = id)
    usercommittee = UserCommitte.objects.get(project_id = id)
    cost_estimate = Cost_Estimate.objects.get(project_id=id)
    
    context = {
        "project":project,
        "usercommittee":usercommittee,
        "cost_estimate":cost_estimate
    }
    
    return render(request,"Open/add_work_order.html",context)