"""
URL configuration for bookstore_project project.

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
from django.urls import path, re_path, include # new
# import sys

# shoes_path = r'C:\Users\ASUS\Desktop\code\books\shoes'
# sys.path.insert(0, shoes_path)

from .views import PatchLogoutView
from allauth.account.views import confirm_email

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from rest_auth.views import PasswordResetConfirmView

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A web API for creating and editing products.'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # Thirtparty allauth 
    path('accounts/', include('allauth.urls')),  # new
    # Pages apps
    path('', include('pages.urls')) ,
    # Pages shoes api
    path('api/shoes/', include('shoes.urls')), 
    # add logout path for api because django 5 not suppose get(api-auth)
    path('api-auth/logout/', PatchLogoutView.as_view()),
    path('api/v1/rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path to add login, logout in apibrowser
    # path('api-auth/', include('rest_framework.urls')),
    # path to django_rest_auth_forked(update) instead django_rest_auth(origin) 
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    # overide account-confirm-email
    path('api/v1/rest-auth/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    #  schema and api docs
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger-docs/', schema_view),
]

