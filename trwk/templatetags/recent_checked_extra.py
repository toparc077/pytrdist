# -*- encoding: utf-8 -*-
from django import template
register = template.Library()
from trwk.libs.request_utils import get_recent_checked
from documents.models import Document
from seminars.models import Seminar


@register.inclusion_tag('sidebar/part-recent-checked.html')
def show_recent_checked(request, **kwargs):
    checked_items = get_recent_checked(request)
    if not checked_items:
        return {'items': None}
    results = []

    #documents
    doc_results = Document.objects.filter(pk__in=[
        item[1]['pk']
        for item in checked_items.items()
        if item[1]['model'] == 'Document'],
        status=1)
    if doc_results:
        for item in doc_results:
            check_time = [
                k for k, v in checked_items.items()
                if v['pk'] == item.pk and v['model'] == 'Document'
            ]
            results.append({'time': check_time[0], 'item': item})

    #seminar
    semi_results = Seminar.objects.filter(pk__in=[
        item[1]['pk']
        for item in checked_items.items()
        if item[1]['model'] == 'Seminar'],
        status=1)
    if semi_results:
        for item in semi_results:
            check_time = [
                k for k, v in checked_items.items()
                if v['pk'] == item.pk and v['model'] == 'Seminar'
            ]
            results.append({'time': check_time[0], 'item': item})

    if results:
        results.sort(key=lambda x: x['time'], reverse=True)
    return {'results': results}
