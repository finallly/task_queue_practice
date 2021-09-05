from django.db import models


class TaskModel(models.Model):
	operation = models.CharField(
		name='operation',
		max_length=32
	)


class LogModel(models.Model):
	date_time = models.DateTimeField(
		name='date_time'
	)
	task = models.ForeignKey(
		TaskModel,
		name='task',
		on_delete=models.PROTECT
	)
