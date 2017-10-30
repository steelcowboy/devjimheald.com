from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from django.contrib import admin
from .models import * 

# Inlines for related models
class ProjectInline(SortableStackedInline):
    model = ProjectPoint

class ProjectAdmin(NonSortableParentAdmin):
    inlines = [
        ProjectInline,
    ]

class EducationInline(SortableStackedInline):
    model = EducationPoint

class EducationAdmin(NonSortableParentAdmin):
    inlines = [
        EducationInline,
    ]

class AffiliationInline(SortableStackedInline):
    model = AffiliationPoint 

class AffiliationAdmin(NonSortableParentAdmin):
    inlines = [
        AffiliationInline,
    ]

class EmploymentInline(SortableStackedInline):
    model = EmploymentPoint 

class EmploymentAdmin(NonSortableParentAdmin):
    inlines = [
        EmploymentInline,
    ]

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Employment, EmploymentAdmin)
