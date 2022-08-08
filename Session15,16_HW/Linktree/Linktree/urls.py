"""Linktree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from linkApp import views
from linkApp.views import AddLinkView, main, AddCategoryView
# from linkApp.views import AddLinkModelView,AddLinkView, main, AddCategoryView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('category', AddCategoryView,  name="category"),
    path('link', AddLinkView,  name="link"),
    # path('modal', AddLinkModelView.as_view(),  name="modal"),
    path('', views.main, name='Linktree' )
    # path('category/<str:category_name>/', views.main,  name="LinkTree"),
]
