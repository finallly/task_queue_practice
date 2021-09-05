# Generated by Django 3.2.7 on 2021-09-04 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queue_manager.taskmodel')),
            ],
        ),
    ]
