"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [ # root urls.py (all the url paths for each app in the project)
    path('admin/', admin.site.urls), 
        # module that defines all the urls that can be requested 
        # from the admin site...
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),

    path('users/', include(('users.urls', 'users'), namespace='users')),
]


# Mapping a URL

# we need a base URL that people can use to access the project
# mapping the base URL to learning log's home page...

# this file represents the entire project

# urlpatterns variable includes sets of urls from the apps in the project.
















