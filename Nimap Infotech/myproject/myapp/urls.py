from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClientViewSet, ProjectViewSet

urlpatterns = [
    # URLs for clients
    path('clients/', ClientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('clients/<int:pk>/', ClientViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    # URLs for projects
    path('clients/<int:client_pk>/projects/', ProjectViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('clients/<int:client_pk>/projects/<int:pk>/', ProjectViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)
