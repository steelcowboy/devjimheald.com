from django.shortcuts import render
from .models import Skill, Project, Education, Affiliation, Employment

# Create your views here.
def index(request):
    return render(request, 'resume/index.html')

def printable(request, tag=None):
    kwargs = {}
    if tag is not None:
        kwargs['tags__name__in'] = [tag]

    skills = Skill.objects.all() 
    projects = Project.objects.filter(**kwargs)
    educations = Education.objects.all()
    affiliations = Affiliation.objects.filter(**kwargs)
    employments = Employment.objects.filter(**kwargs)

    context = {
            'skills': skills, 
            'projects': projects, 
            'educations': educations, 
            'affiliations': affiliations,
            'employments': employments
            }

    return render(request, 'resume/printable.html', context)