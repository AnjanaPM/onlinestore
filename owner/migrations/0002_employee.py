# Generated by Django 4.0.1 on 2022-02-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField(max_length=6)),
                ('experience', models.PositiveIntegerField(max_length=10)),
            ],
        ),
    ]