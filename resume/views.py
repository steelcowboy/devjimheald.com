from django.shortcuts import render
from .models import Skill, Experience, Education, Affiliation, Employment

# Create your views here.
def index(request):
    return render(request, 'resume/index.html')

def printable(request):
    skills = Skill.objects.all() 
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    affiliations = Affiliation.objects.all()
    employments = Employment.objects.all()

    context = {
            'skills': skills, 
            'experiences': experiences, 
            'educations': educations, 
            'affiliations': affiliations,
            'employments': employments
            }

    return render(request, 'resume/printable.html', context)
