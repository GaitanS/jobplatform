from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    open_to_work_choices = (('yes', 'Da'), ('no', 'Nu'))

    phone = models.CharField('telefon:', max_length=15)
    city = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    open_to_work = models.CharField(max_length=10, choices=open_to_work_choices, default='no',
                                    null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='static/users/profile', null=True, blank=True)
    about = models.TextField(max_length=2000, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Ad(models.Model):
    job_type = (('full_time', 'Full time'), ('part_time', 'Part time'), ('project', 'Temporar'), ('others', 'Altele'))
    contract_type = (('determined', 'Determinat'), ('undetermined', 'Nedeterminat'), ('internship', 'Internship'),
                     ('collaboration', 'Colaborare'))
    education = (('unqualified', 'Necalificat'), ('qualified', 'Calificat'), ('student', 'Student'))
    local_or_distance = (('local', 'La fața locului'), ('distance', 'De la distanță'), ('hibrid', 'Regim hibrid'))
    salary_type = (('lei', 'Lei'), ('euro', 'Euro'), ('dolar', 'Dolari'))
    experience = (
        ('trainee', 'Stagiar'), ('beginner', 'Începător (< 2ani)'), ('mediu', 'Nivel mediu de experienta (2-5 ani)'),
        ('senior', 'Senior-level (> 5ani)'), ('manager', 'Manager / Executiv'))

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    salary = models.IntegerField()
    salary_type = models.CharField(max_length=10, choices=salary_type)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=10, choices=job_type, null=True, blank=True)
    contract_type = models.CharField(max_length=15, choices=contract_type)
    education = models.CharField(max_length=15, choices=education)
    local_or_distance = models.CharField(max_length=10, choices=local_or_distance)
    experience = models.CharField(max_length=10, choices=experience)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/ad', null=True, blank=True)
    active = models.BooleanField(default=True)
    phone = models.CharField('telefon:', max_length=15)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'
