"""
URL configuration for pollsapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # Added include import
from django.urls import re_path # Added re_path import for regular expression URL patterns

urlpatterns = [
    path('admin/', admin.site.urls), # Admin URL
    re_path(r'^', include('polls.urls')), # Include polls app URLs with a prefix
]

# Explanation:
# - The first pattern directs requests to the Django admin site.
# - The second pattern includes URLs from the 'polls' app, prefixed with 'polls/'.
#   This means that any URL starting with 'polls/' will be handled by the URLs defined in 'polls.urls'.
#   This allows for better organization and separation of concerns in your URL configuration.