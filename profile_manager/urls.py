# from profile_manager import views
# from rest_framework import routers
#
#
# router = routers.DefaultRouter()
# router.register(r'create_provider', views.provider_list)
# router.register(r'^providers/(?P<pk>[0-9]+)$', views.provider_detail)
#
# urlpatterns = router.urls


#-----

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profile_manager import views

urlpatterns = [
    url(r'^create_provider/$', views.provider_list),
    url(r'^provider/(?P<id>[0-9]+)$', views.provider_detail),
    url(r'^providers/$', views.provider_list),
    url(r'^category/$', views.category_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)