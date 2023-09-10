from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('category=<str:slug>',views.category,name="category"),
    path('detail/<str:slug>',views.detail,name="detail"),
    path('service_detail/<str:slug>',views.service_detail,name="servic_detail"),
    # path('category/<str:slug>', views.category,name="category"),
    # path('category=<int:id>', views.category,name="category"),
    path('current_job_oppening', views.job_oppening,name="job_oppening"),
    path('contact', views.contact,name="contact"),
    path('apply', views.apply,name="apply"),
    path('userlogin', views.userlogin,name="userlogin"),
    path('signup', views.signup,name="signup"),
    path('userlogout', views.userlogout,name="userlogout"),
    path('resume', views.resume,name="resume"),
    path('search', views.search,name="search"),
    
]