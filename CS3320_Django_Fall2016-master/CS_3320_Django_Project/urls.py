"""CS_3320_Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from vibenjive import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('vibenjive.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'login/req/', views.auth_view),
    url(r'signup/req/', views.auth_reg),
    url(r'update_password/', views.update_password, name='update_password'),
    url(r'^accountmanagement/$', views.account_management),
    url(r'^del_user/', views.del_user),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^add_user_info/', views.add_user_info, name='add_user_info')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
