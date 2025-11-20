from django.urls import path 

from . import views 

urlpatterns = [
        path("",views.index , name="index"),
            #path , func in views.py , name of file
        path("results",views.show_results, name = "results"),
            
        ]
