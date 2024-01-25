from django.db import models

# Create your models here.
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
import json

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
        (2, 'CAO'),
        (3, 'ACCOUNTANT'),
        (4, 'ENGINEER'),
        (5, 'SUBENGINEER'),
        (6, 'PLANNINGOFFICER'),
        (7, 'WARDSACHIB'),

    )
   
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    
    
class Cao(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    status = models.CharField(default="Active", null=True, max_length=200)
    
    def __str__(self):
        return self.name
    
class Accountant(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    status = models.CharField(default="Active", null=True, max_length=200)
    

    def __str__(self):
        return self.name
    
class Engineer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    status = models.CharField(default="Active", null=True, max_length=200)
    def __str__(self):
        return self.name
    
class Ward(models.Model):
    name = models.CharField(max_length=250)
    chairperson = models.CharField(max_length=250, null = True)
    def __str__(self):
        return self.name
    
    
    
class PlanningOfficer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    status = models.CharField(default="Active", null=True, max_length=200)
    def __str__(self):
        return self.name
    
class SubEngineer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    wards = models.ManyToManyField(Ward)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    status = models.CharField(default="Active", null=True, max_length=200)
    def __str__(self):
        return self.name
    
class Wadasachib(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    wards = models.ManyToManyField(Ward)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    status = models.CharField(default="Active", null=True, max_length=200)
    def __str__(self):
        return self.name
    
from django.db import models

class FiscalYear(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CurrentFiscalYear(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"Current Fiscal Year: {self.fiscal_year.name}"

    def save(self, *args, **kwargs):
        # Set fiscal_year to the latest FiscalYear object
        latest_fiscal_year = FiscalYear.objects.latest('id')
        self.fiscal_year = latest_fiscal_year
        super().save(*args, **kwargs)
class Budget_Type(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name   
    
    
class Procurement_Type(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    fiscalyear = models.ForeignKey(CurrentFiscalYear, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    procurement_type = models.ForeignKey(Procurement_Type, on_delete=models.CASCADE, null=True)
    budget_type = models.ForeignKey(Budget_Type, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=250)
    budget = models.FloatField()
    status = models.IntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    accomplish_date = models.DateField(blank=True, null=True)
    extended_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # If the project is being created and accomplish_date is not set,
        # set accomplish_date to the initial value of extended_date
        if not self.pk and not self.accomplish_date:
            self.accomplish_date = self.extended_date

        super().save(*args, **kwargs)
    

    
class UserCommitte(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    formation_date =  models.DateField(null=True)
    name = models.CharField(max_length=250)
    chairman_name = models.CharField(max_length=250)
    chairman_citizenship = models.CharField(max_length=250, null=True)
    chairman_mobile = models.CharField(max_length=250, null=True)
    secretary_name = models.CharField(max_length=250)
    secretary_citizenship = models.CharField(max_length=250, null=True)
    secretary_mobile = models.CharField(max_length=250, null=True)
    treasurer_name = models.CharField(max_length=250)
    treasurer_citizenship = models.CharField(max_length=250, null=True)
    treasurer_mobile = models.CharField(max_length=250, null=True)
    status = models.IntegerField(default=0,null=True)
    member1 = models.CharField(max_length=250,null=True)
    member2 = models.CharField(max_length=250,null=True)
    member3 = models.CharField(max_length=250,null=True)
    member4 = models.CharField(max_length=250,null=True)

    def get_members(self):
        # Deserialize the JSON data to retrieve the list of members
        return json.loads(self.members) if self.members else []

    def set_members(self, members):
        # Serialize the list of members to store in the TextField
        self.members = json.dumps(members)

    def __str__(self):
        return self.name
    
class Cost_Estimate(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    budget = models.FloatField()
    contigency_amount = models.FloatField()
    user_contribution = models.FloatField()
    cost_estimate = models.FloatField()

    def __str__(self):
        return self.project.name
    
    @property
    def office_contribution(self):
        return self.budget - self.contigency_amount

    
    
    
