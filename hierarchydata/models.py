from django.db import models


class HierarchyData(models.Model):
    si_no = models.IntegerField()
    title = models.CharField(max_length=32)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
