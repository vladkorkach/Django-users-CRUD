from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^user/create/$', views.UserCreate.as_view(), name='create-user'),
    url(r'^user/(?P<pk>\d+)/edit/$', views.UserUpdate.as_view(), name='user-edit'),
    url(r'^user/(?P<pk>\d+)/remove/$', views.UserRemove.as_view(), name='remove-user'),
    url(r'^user/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^user/export_csv/$', views.export_users_csv, name='export-users-csv'),
]
