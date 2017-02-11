from django.conf.urls import url
from vibenjive import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'updateemail/$', views.update_email, name='updateemail'),
    url(r'ch_email/$', views.ch_email, name='ch_email'),
    url(r'email_error/$', views.email_error, name='email_error'),
    url(r'updateinfo/$', views.update_info, name='updateinfo'),
    url(r'ch_info/$', views.ch_info, name='ch_info'),
    url(r'updatepassword/$', views.chpasswd, name='updatepassword'),
    url(r'^searchresults/', views.search),
    url(r'^accountmanagement/$', views.account_management, name='accountmanagement'),
    url(r'deleteaccount/$', views.delete_account, name='deleteaccount'),
    url(r'searchresults/$', views.search, name='searchresults'),
    url(r'logout/$', views.logout, name="logout"),
    url(r'login_error/$', views.login_error, name="login_error"),
    url(r'update_success/$', views.update_success, name="update_success"),
    url(r'delete_account_success/$', views.delete_account_success, name="delete_account_success"),
    url(r'add_music/$', views.add_music, name="add_music"),
    url(r'uploadaudio/$', views.uploadaudio, name="uploadaudio"),
    url(r'uploadaudio_success/$', views.uploadaudio_success, name="uploadaudio_success"),
    url(r'manageaudio/$', views.manageaudio, name="manageaudio"),
    url(r'deleteaudio_success/$', views.deleteaudio_success, name="deleteaudio_success"),
    url(r'del_music/$', views.del_music, name="del_music"),
    url(r'sendemail/$', views.sendemail, name="sendemail"),
    url(r'email_success/$', views.email_success, name="email_success"),





]
