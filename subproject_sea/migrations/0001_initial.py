# Generated by Django 4.2.2 on 2023-07-03 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Categoryid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Categorydescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('Levelid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Leveldescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Studentid', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('Studentname', models.CharField(max_length=100)),
                ('Studentprogramme', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Award', models.CharField(max_length=100)),
                ('Achievement_date', models.DateField()),
                ('Event', models.CharField(max_length=100)),
                ('Categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subproject_sea.category')),
                ('Levelid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subproject_sea.level')),
                ('Studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subproject_sea.student')),
            ],
        ),
    ]