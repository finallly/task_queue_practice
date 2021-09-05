from django.db import models

from queue_manager.models import TaskModel


class WorkerModel(models.Model):
	is_working = models.BooleanField(
		name='is_working'
	)
	current_task = models.ForeignKey(
		TaskModel,
		name='task',
		on_delete=models.PROTECT
	)
