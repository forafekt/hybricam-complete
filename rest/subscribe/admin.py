import csv

from django.contrib import admin
from django.http import HttpResponse

from rest.subscribe.models import Subscribe


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        """
        Export CSV
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class EmailSubscribeAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['email', 'firstName', 'lastName', 'accepted', 'id']
    list_filter = ('email', 'firstName', 'lastName', 'accepted', 'id')
    search_fields = ['email', 'firstName', 'lastName', 'id']
    actions = ["export_as_csv"]


admin.site.register(Subscribe, EmailSubscribeAdmin)
