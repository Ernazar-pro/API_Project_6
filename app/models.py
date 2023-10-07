from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null=True, max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    members = models.ManyToManyField(User, related_name='project_2')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Проекта'
        verbose_name_plural = 'Проекты'

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    deadline_date = models.DateField(blank=True, null=True, auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
