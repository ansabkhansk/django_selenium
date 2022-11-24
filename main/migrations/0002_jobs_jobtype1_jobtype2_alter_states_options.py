# Generated by Django 4.1.3 on 2022-11-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.AutoField(db_column='Job_ID', primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, db_column='Company_Name', max_length=50, null=True)),
                ('position', models.CharField(blank=True, db_column='Position', max_length=50, null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=50, null=True)),
            ],
            options={
                'db_table': 'jobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobtype1',
            fields=[
                ('category_id', models.AutoField(db_column='Category_ID', primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=50, null=True)),
            ],
            options={
                'db_table': 'jobtype1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobtype2',
            fields=[
                ('sub_category_id', models.AutoField(db_column='Sub_Category_ID', primary_key=True, serialize=False)),
                ('sub_category', models.CharField(blank=True, db_column='Sub_Category', max_length=50, null=True)),
            ],
            options={
                'db_table': 'jobtype2',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='states',
            options={'managed': False},
        ),
    ]