# Generated by Django 4.1.3 on 2022-11-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'states',
            },
        ),
    ]
