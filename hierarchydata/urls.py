from django.urls import path
from .views import HierarchyView

urlpatterns = [
    path('data/', HierarchyView.as_view(), name='data'),
]
