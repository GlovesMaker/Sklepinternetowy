from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^zwrot/$', views.zwrot, name='zwrot'),
    url(r'^koszt/$', views.koszt, name='koszt'),
    #url(r'^regulamin/$', views.regulamin, name='regulamin'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
]

