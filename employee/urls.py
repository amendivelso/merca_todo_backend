from django.conf.urls import url 
from employee import views 
 
urlpatterns = [ 
    url(r'^api/employees$', views.employees_list),
    url(r'^api/employees/(?P<pk>[0-9]+)$', views.employee_detail),
    url(r'^api/employees/admin$', views.employees_list_admin),
    url(r'^api/employees/noadmin$', views.employees_list_user)
]
