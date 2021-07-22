from django.shortcuts import render
from .models import HierarchyData
from django.views import generic

# Create your views here.
class HierarchyView(generic.ListView):
    template_name = 'hierarchy.html'

    def get_queryset(self):
        return HierarchyData.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HierarchyView, self).get_context_data(**kwargs)
        context['main'] = self.get_queryset().filter(parent_id__isnull=True)
        context['sub'] = self.get_queryset().filter(parent_id__in=context['main'])
        context['sub_sub'] = self.get_queryset().filter(parent_id__in=context['sub'])
        return context
