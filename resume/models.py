from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

# Base models
class Event(models.Model):
    archived = models.BooleanField('Archived')
    start_date = models.DateField('Start Time')
    ongoing = models.BooleanField('Ongoing')
    end_date = models.DateField('End Time', null=True, blank=True)

    class Meta:
        ordering = ['-start_date']
        abstract = True

class EventPoint(SortableMixin):
    archived = models.BooleanField('Archived')
    text = models.CharField('Text', max_length=100)

    class Meta:
        ordering = ['point_order']
        verbose_name_plural = None 
        abstract = True

    point_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

# Real models
class Skill(models.Model):
    archived = models.BooleanField('Archived')
    keyword = models.CharField('Keyword', max_length=25)
    text = models.TextField('Text')
    archived = models.BooleanField('Archived')

    def __str__(self):
        return self.keyword 

class Project(Event):
    name = models.CharField('Project Name', max_length=50)
    exp_type = models.CharField('Project Type', max_length=20)

    def __str__(self):
        return self.name

class ProjectPoint(EventPoint):
    experience = SortableForeignKey(Project, null=True)
    
    class Project(EventPoint.Meta):
        verbose_name_plural = "Project Points"

class Education(Event):
    school = models.CharField('Institution', max_length=100)
    graduation = models.DateField('Graduation')
    degree = models.CharField('Degree', max_length=100)
    gpa = models.FloatField('GPA')

    def __str__(self):
        return self.school

class EducationPoint(EventPoint):
    education = SortableForeignKey(Education, null=True)
    text = models.TextField('Text')
    keyword = models.CharField('Keyword', max_length=50, null=True)

    class Meta(EventPoint.Meta):
        verbose_name_plural = "Education Points"

class Affiliation(Event):
    name = models.CharField('Affiliation', max_length=100)

    def __str__(self):
        return self.name

class AffiliationPoint(EventPoint):
    affiliation = SortableForeignKey(Affiliation, null=True)

    class Meta(EventPoint.Meta):
        verbose_name_plural = "Affiliation Points"

class Employment(Event):
    name = models.CharField('Institution', max_length=100)

    def __str__(self):
        return self.name

class EmploymentPoint(EventPoint):
    employment = SortableForeignKey(Employment, null=True)

    class Meta(EventPoint.Meta):
        verbose_name_plural = "Employment Points"
