
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .import views, Cao_Views, Poff_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    
    
    
    
    path('Cao/Home', Cao_Views.Home, name='cao_home'),   
    path('Cao/Add/Accountant', Cao_Views.ADD_ACCOUNTANT, name='add_accountant'),   
    path('Cao/Add/Engineer', Cao_Views.ADD_ENGINEER, name='add_engineer'),   
    path('Cao/Add/PlanningOfficer', Cao_Views.ADD_PLANNINGOFFICER, name='add_planningofficer'),   
    path('Cao/Add/SubEngineer', Cao_Views.ADD_SUBENGINEER, name='add_subengineer'),   
    path('Cao/Add/WadaSachib', Cao_Views.ADD_WADASACHIB, name='add_wadasachib'),   
    path('Cao/View/Accountant', Cao_Views.VIEW_ACCOUNTANT, name='view_accountant'), 
    path('Cao/View/Engineer', Cao_Views.VIEW_ENGINEER, name='view_engineer'), 
    path('Cao/View/SubEngineer', Cao_Views.VIEW_SUBENGINEER, name='view_subengineer'), 
    path('Cao/View/PlanningOfficer', Cao_Views.VIEW_PLANNINGOFFICER, name='view_planningofficer'), 
    path('Cao/View/Wadasachib', Cao_Views.VIEW_WADASACHIB, name='view_wadasachib'), 
    
    
    
    
    path('PlanningOfficer/Home', Poff_Views.Home, name='poff_home'),   
    
    path('PlanningOfficer/Add/Project', Poff_Views.ADD_PROJECT, name='add_project'),  
    path('PlanningOfficer/Print/Contract/Document', Poff_Views.PRINT_CONTRACT_DOCUMENT, name='print_contract_document'),  
    
    
    
    
    
    
    # this is for all type of user
    path('View/Projects', views.VIEW_PROJECTS, name='view_projects'), 
    path('Add/UserCommittee', views.ADD_USERCOMMITTEE, name='add_usercommittee'), 
    path('View/UserCommittee', views.VIEW_USERCOMMITTEE, name='view_usercommittee'), 
    path('Add/Contract', views.ADD_CONTRACT, name='add_contract'), 
    path('View/CostEsimate', views.VIEW_COST_ESTIMATE, name='view_cost_estimat'), 
    path('View/Photo/CostEsimate/<int:id>/', views.VIEW_PHOTO_COST_ESTIMATE, name='view_photo_cost_estimate'), 
    path('Print/Contract/Document/<str:id>/', views.PRINT_CONTRACT_DOCUMENT, name='print_documents'), 
    path('Print/Tippani/Document/<str:id>/', views.PRINT_TIPPANI, name='print_tippani'), 
    path('Print/Bank/Letter/<str:id>/', views.PRINT_BANK_LETTER, name='print_bank_letter'), 
    path('Print/Work/Order/<str:id>/', views.PRINT_WORK_ORDER, name='print_work_order'), 
    
    
    
    
    
    
    path('View/Estimated/Project', views.VIEW_ESTIMATED_PROJECT, name='view_estimated_project'), 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ajax 
    path('ajax/load-user-committee/', views.LOAD_USER_COMMITTEE, name = "ajax_load_user_committee"),
    path('ajax/load-cost-committee/', views.LOAD_COST_COMMITTEE, name = "ajax_load_cost_estimate"),
    path('ajax/load-budget/', views.LOAD_BUDGET, name = "ajax_load_budget"),
    path('ajax/load-contingency/', views.LOAD_CONTINGENCY, name = "ajax_load_contingency"),
    path('ajax/load-user-contribution/', views.LOAD_USER_CONTRIBUTION, name = "ajax_load_usercontribution"),
    
    
    
    
    
    
    
    
    
    
    # this is for engineer
    path('Engineer/Add/CostEstimate', views.ADD_COST_ESTIMATE, name='add_cost_estimate'), 
    
    
    
    
    
   
    
    
    
    
    
     
    
    
    
    
    
    
    
    
 # export to excel 
    path('export_projects_to_excel', views.export_projects_to_excel, name='export_projects_to_excel'),
    path('import_excel/', views.import_excel, name='import_excel'),
    
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

