from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('laptops/', display_laptops, name='display_laptops'),
    path('desktops/', display_desktops, name='display_desktops'),
    path('mobiles/', display_mobiles, name='display_mobiles'),

    path('add_laptop/', add_laptop, name='add_laptop'),
    path('add_desktop/', add_desktop, name='add_desktop'),
    path('add_mobile/', add_mobile, name='add_mobile'),

    re_path(r'^laptops/edit_item/(?P<pk>\d+)/$', edit_laptop, name='edit_laptop'),
    re_path(r'^desktops/edit_item/(?P<pk>\d+)/$', edit_desktop, name='edit_desktop'),
    re_path(r'^mobiles/edit_item/(?P<pk>\d+)/$', edit_mobile, name='edit_mobile'),

    re_path(r'^laptops/delete/(?P<pk>\d+)/$', delete_laptop, name='delete_laptop'),
    re_path(r'^desktops/delete/(?P<pk>\d+)/$', delete_desktop, name='delete_desktop'),
    re_path(r'^mobiles/delete/(?P<pk>\d+)/$', delete_mobile, name='delete_mobile'),
]

