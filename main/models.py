from django.db import models

# Create your models here.

# class Companyprofile(models.Model): #CompanyProfile
#     company_id = models.AutoField(db_column='Company_ID', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sub_category = models.CharField(db_column='Sub_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sub_category_0 = models.ForeignKey('Jobtype2', models.DO_NOTHING, db_column='Sub_Category_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.

#     class Meta:
#         managed = False
#         db_table = 'companyprofile'

class Jobs(models.Model): #Jobs
    job_id = models.AutoField(db_column='Job_ID', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # company = models.ForeignKey(Companyprofile, models.DO_NOTHING, db_column='Company_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobs'


class Jobtype1(models.Model): #Categories
    category_id = models.AutoField(db_column='Category_ID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobtype1'


class Jobtype2(models.Model): #Subcategories
    sub_category_id = models.AutoField(db_column='Sub_Category_ID', primary_key=True)  # Field name made lowercase.
    sub_category = models.CharField(db_column='Sub_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Jobtype1, models.DO_NOTHING, db_column='Category_ID', blank=True, null=True,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobtype2'


class States(models.Model): #States
    state_id = models.AutoField(db_column='State_ID', primary_key=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'states'