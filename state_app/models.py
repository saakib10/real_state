from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE


class Clients(models.Model):
    client_name = models.CharField(max_length=30, null=True, blank=True)
    client_image = models.ImageField(null=True, blank=True)
    testimonial = models.TextField(blank=True, null=True)
    writer = models.CharField(max_length=30, null=True, blank=True)
    designation = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.client_name

    def get_clients():
        return Clients.objects.all()

    @property
    def imagesURL(self):
        try:
            url = self.client_image.url
        except:
            url = ''
        return url

class EmployeeTeam(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    designation = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    f_link = models.CharField(max_length=50, blank=True, null=True)
    l_lisk = models.CharField(max_length=50, blank=True, null=True)
    t_link = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_employee():
        return EmployeeTeam.objects.all()

    @property
    def imagesURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ProjectType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_all_type():
        return ProjectType.objects.all()

class ProjectStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_all_status():
        return ProjectStatus.objects.all()



class Projects(models.Model):

    # Project details

    name = models.CharField(null=True, blank=True, max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    feature_image = models.FileField(null=True, blank=True)
    status = models.ForeignKey(ProjectStatus, on_delete=CASCADE)
    type = models.ForeignKey(ProjectType, on_delete=CASCADE)
    floor = models.IntegerField(blank=True, null=True)
    apartment = models.IntegerField(blank=True, null=True)
    size_of_apartment = models.CharField(max_length=50)
    facing = models.CharField(max_length=30)
    basement = models.IntegerField(blank=True, null=True)
    parking = models.IntegerField(blank=True, null=True)
    razuk_no = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    completed_per = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_all_projects():
        return Projects.objects.all()

    @staticmethod
    def get_project_with_status(status):
        if status:
            return Projects.objects.filter(status = status)
        else:
            return Projects.get_all_projects()

    
class ProjectImages(models.Model):
    project = models.ForeignKey(Projects,default=None,on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.project.name

class ProjectFeatures(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, default=None)
    feature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.project.name


class HomePageSlider(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class FloorMap(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=30)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.project.name

class NearbyInstitute(models.Model):
    CATEGORY_CHOICES = (
        ('S', 'School'),
        ('H', 'Hospital'),
        ('E', 'Education'),
        ('O', 'Other')
    )
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True,blank=True)
    

    def __str__(self):
        return self.project.name

class ProjectNearbyInstitute(models.Model):
    CATEGORY_CHOICES = (
        ('S', 'School'),
        ('H', 'Hospital'),
        ('E', 'Education'),
        ('O', 'Other')
    )
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, default="")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True,blank=True)
    

    def __str__(self):
        return self.project.name