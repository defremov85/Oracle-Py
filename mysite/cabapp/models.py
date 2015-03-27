# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Tool(models.Model):
    gcmid = models.CharField(max_length=20, blank=True, primary_key=True)
    narid = models.CharField(max_length=255, blank=True)
    urgency = models.CharField(max_length=20, blank=True)
    implementer_group = models.CharField(max_length=255, blank=True)
    approver_group = models.CharField(max_length=255, blank=True)
    ci_list = models.CharField(max_length=255, blank=True)
    created_date = models.DateField(blank=True, null=True)
    planned_date = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=3000, blank=True)
    flag = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tools'

    def __str__(self):              # __unicode__ on Python 2
        return self.name
