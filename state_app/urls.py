from . import views
from django.urls import path
from state_app.views import GetProductSearch, GetProductView,TutorialView

urlpatterns = [
    path('', views.home_page_render, name='home_page'),
    path('team/', views.team_page_render, name='team_page'),
    path('about_us/',views.about_us_page_render, name='about_us'),
    path('career/',views.career_page_render, name='career'),
    path('buyer/',views.buyer_page_render, name='buyer'),
    path('landowner/',views.landowner_page_render, name='landowner'),
    path('project/',views.project_page_render, name='project'),
    path('contact-us/',views.contact_us_page_render, name='contact_us'),
    path('project/<int:id>/',views.project_details_render, name='project_view'),
    # path('project_2/',views.project_with_ajax, name='project_2'),
    path('/project_2', TutorialView.as_view(), name="index"),
    path('/project_2/test', GetProductView.as_view(), name="status"),
    path('/project_2/search', GetProductSearch.as_view(), name="search"), 
]