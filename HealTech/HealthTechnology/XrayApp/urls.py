from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 url(r'lo',views.DiagnoseXray,name="Diagnosis"),
 url(r'login/',views.loginView,name="login_view"),
 url('', views.prediction, name='prediction'),

]