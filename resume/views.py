from typing import List, Dict, Any, Optional

from django.shortcuts import render
from django.views import View
from .models import Skill, Project, Education, Affiliation, Employment


OptStr = Optional[str]


class IndexView(View):
    def get(self, request):
        return render(request, 'resume/index.html')

class PrintableView(View):
    NO_TAGS = [Affiliation]

    def _get_section_list(self, section) -> List[Dict[str, Any]]:
        sect_name = section.__name__.lower()
        points_attr = f"{sect_name}point_set"

        filter_args = {'archived': False}  # Filter archived objects
        if self.tag is not None and section not in self.NO_TAGS:
            filter_args['tags__name__in'] = [self.tag]
        
        return [
            {
                "object": obj,
                "points": getattr(obj, points_attr).filter(**filter_args)
            }
            for obj in section.objects.filter(**filter_args)
        ]

    def get(self, request, tag=None):
        self.tag = tag

        skills = Skill.objects.all() 
        educations = Education.objects.all()

        projects = self._get_section_list(Project) 
        affiliations = self._get_section_list(Affiliation)
        employments = self._get_section_list(Employment)

        context = {
                'skills': skills, 
                'projects': projects, 
                'educations': educations, 
                'affiliations': affiliations,
                'employments': employments
                }

        return render(request, 'resume/printable.html', context)