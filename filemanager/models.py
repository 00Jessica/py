from django.db import models
from django.utils import timezone


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    gender = models.CharField(max_length=10, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    password = models.CharField(max_length=100, null=False, blank=False)
    is_admin = models.CharField(max_length=1, choices=[("Y", "Yes"), ("N", "No")])

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    remark = models.TextField(blank=True)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True)
    upload_date = models.DateField(default=timezone.now)
    remark = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    upload_date = models.DateField(default=timezone.now)
    remark = models.TextField(blank=True)

    def __str__(self):
        return self.name
