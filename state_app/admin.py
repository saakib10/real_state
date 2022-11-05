from django.contrib import admin

from .models import *

admin.site.register(ProjectType)
admin.site.register(Clients)
admin.site.register(EmployeeTeam)
admin.site.register(ProjectStatus)

class ProjectFeaturesAdmin(admin.TabularInline):
    model = ProjectFeatures

class ProjectImageAdmin(admin.TabularInline):
    model = ProjectImages

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]
    inlines = [ProjectFeaturesAdmin]

    class Meta:
       model = Projects

@admin.register(ProjectImages)
class ProjectImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjectFeatures)
class ProjectFeaturesAdmin(admin.ModelAdmin):
    pass

admin.site.register(HomePageSlider)
admin.site.register(ProjectNearbyInstitute)
admin.site.register(FloorMap)
