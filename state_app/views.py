from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.http import JsonResponse
from django.views import View

from state_app.models import Clients, EmployeeTeam, FloorMap, HomePageSlider, ProjectFeatures, ProjectImages, ProjectStatus, Projects

def home_page_render(request):
    clients = Clients.get_clients()
    slider = HomePageSlider.objects.all()
    projects = Projects.objects.all()
    

    contex = {'clients': clients, 'slider':slider,'projects':projects}
    return render(request,'index.html',contex)

def team_page_render(request):
    employee = EmployeeTeam.get_employee()
    status = ProjectStatus.objects.all()
    contex = {'employee':employee,'status':status}
    return render(request,'team.html',contex)

def about_us_page_render(request):
    clients = Clients.get_clients()
    status = ProjectStatus.objects.all()
    contex = {'clients': clients,'status':status}
    return render(request,'about_us.html',contex)

def career_page_render(request):
    return render(request,'career.html')

def buyer_page_render(request):
    return render(request,'buyer.html')

def landowner_page_render(request):
    return render(request,'landowner.html')

def contact_us_page_render(request):
    return render(request,'contact_us.html')

def project_page_render(request):
    status = ProjectStatus.objects.all()
    projects = None
    status_id = request.GET.get('status')
    if status_id:
        projects = Projects.get_project_with_status(status_id)
    else:
        projects = Projects.get_all_projects()
        
    contex = {'projects':projects,'status':status}
    return render(request,'project.html',contex)

def project_details_render(request, id):
    project = Projects.objects.get(pk = id)
    images = ProjectImages.objects.filter(project = project)
    status = ProjectStatus.objects.all()
    features = ProjectFeatures.objects.filter(project = project)
    projects = Projects.objects.all()
    floor = FloorMap.objects.filter(project = project)
    contex = {'project': project,'images':images,'status':status,'features':features,'projects':projects,'floor':floor}
    return render(request,'project_view.html',contex)

# def project_with_ajax(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         item = Projects.objects.values()
#         user_items = list(item)
#         return JsonResponse({'items': user_items})
#     return render(request,'project_2.html')

class TutorialView(View):
    def get(self,request, *args, **kwargs):
        status = ProjectStatus.objects.all()
        context = {'status' : status }
        return render(request,'project_2.html',context)

class GetProductView(View):

    def get(self,request,*args, **kwargs):
        if request.is_ajax():
            status = self.request.GET.get("status")
            products = Projects.objects.filter(status = status).values()
            return JsonResponse({'data': list(products)})
        return HttpResponse('Wrong request')

class GetProductSearch(View):

    def get(self,request,*args, **kwargs):
        if request.is_ajax():
            status = self.request.GET.get("name")
            products = Projects.objects.filter(name__contains = status).values()
            print(products)
            print(Projects.objects.filter(name__contains = status).values().query)
            return JsonResponse({'data': list(products)})
        return HttpResponse('Wrong request')

    
