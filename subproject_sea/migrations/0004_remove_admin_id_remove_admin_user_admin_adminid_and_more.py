# Generated by Django 4.2.2 on 2023-07-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subproject_sea', '0003_rename_full_name_admin_name_remove_admin_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.AddField(
            model_name='admin',
            name='adminid',
            field=models.CharField(default=1, max_length=5, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='apassword',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Spassword',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
