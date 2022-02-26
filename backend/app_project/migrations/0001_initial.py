# Generated by Django 4.0.2 on 2022-02-26 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('project_name', models.CharField(max_length=50, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, null=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(default='', max_length=100, verbose_name='类名')),
                ('class_doc', models.TextField(blank=True, default='', null=True, verbose_name='类描述')),
                ('case_name', models.CharField(default='', max_length=100, verbose_name='方法名')),
                ('case_doc', models.TextField(blank=True, default='', null=True, verbose_name='方法描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_project.file')),
            ],
        ),
    ]
