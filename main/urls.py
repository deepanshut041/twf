
from django.conf.urls import re_path, include, url
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions

from .views import CenterView, CenterDistanceView, ProductView, LoadView, LoadDistanceView, OrderView

api_set_router = routers.DefaultRouter()
api_set_router.register(r'centers', CenterView)
api_set_router.register(r'cdistances', CenterDistanceView)
api_set_router.register(r'products',  ProductView)
api_set_router.register(r'loads', LoadView)
api_set_router.register(r'ldistances', LoadDistanceView)
api_set_router.register(r'orders', OrderView)

urlpatterns = [
   url(r'^', include(api_set_router.urls), name='api'),
   url(r'^docs/', include_docs_urls(title="api-doc", public=True, permission_classes=[])),
]