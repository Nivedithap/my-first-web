from django.urls import path
from . import views
from django.contrib.auth.views import login,logout
from django.conf.urls.static import static
from django.conf import settings
app_name = 'waste'
urlpatterns = [
    path('prod', views.prod_list, name='prod_list'),
    path('',views.mainpage,name='main_page'),
    path('login/',login,{'template_name':'waste/login.html'}),
        path('logout/',logout,name='logout'),
    path('register/',views.register,name='register'),
    path('about/',views.about,name='about_us'),
    path('contact/',views.contact,name='contact'),
    path('blogs/',views.blog,name='blog'),
    path('myprod/',views.myprod_list,name='myprod_list'),
    path('myprod/addprod/',views.addprod,name='add_prod'),
   
     path('myprod/activate/<int:product_id>',views.activate,name='activate'),
    path('myprod/deactivate/<int:product_id>',views.deactivate,name='deactivate'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
