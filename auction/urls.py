from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^signup/$',views.signup),
    url(r'^login/$', views.login_view),
    url(r'^items/$', views.items_view),
    url(r'^additem/$', views.additems_view),
    url(r'^myitems/$', views.myitems_view),
    url(r'^deleteitem/(?P<id>[0-9]+)$', views.delete_view),
    url(r'^itemdetail/(?P<id>[0-9]+)$', views.itemdetail_view),
    url(r'^myitems/(?P<id>[0-9]+)$', views.bids_view),
]