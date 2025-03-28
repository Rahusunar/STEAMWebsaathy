# Generated by Django 4.2.16 on 2024-10-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodingClassEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('course_level', models.CharField(choices=[('basic', 'Basic Level of Coding'), ('advanced', 'Advanced Level of Coding'), ('basic-advance', 'Basic to Advance Level of Coding')], max_length=50)),
            ],
        ),
    ]
