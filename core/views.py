from json import dumps

from django.http import HttpResponse
from django.shortcuts import render

from tips.core.models import Tag
from tips.core.models import Tip
from tips.core.models import Vote
# Create your views here.

def get_tags(request):

    tags = []
    for tag in Tag.objects.all():
        tags.append(tag.text)

    return HttpResponse(dumps({'tags': tags}),
                        content_type='application/json')


def get_tips(request):
    PAGE_SIZE = 30

    tag_id = request.GET.get('tag_id', None)
    sort_order = request.GET.get('sort_order', 'time')
    page = request.GET.get(page, 0)

    tips = Tip.objects.all()
    if tag_id is not None:
        tips = tips.filter(tags__id=tag_id)
    if sort_order == 'time':
        tips = tips.order_by('submit_time')
    tips = tips[page * PAGE_SIZE: (page+1) * PAGE_SIZE]

    json_tips = []
    for tip in tips:
        json_tips.append(tip.to_json())

    return HttpResponse(dumps({'tips': tips}),
                        content_type='application/json')


def vote(request):
    tip = Tip.objects.get(pk=request.GET['tip_id'])
    ip_addr = request.META['REMOTE_ADDR']

    vote = Vote(tip=tip, ip_addr=ip_addr)
    # TODO: return proper HTML codes
    try:
        vote.save()
        response = {'status': 'Success'}
    except:
        # might fail to a duplicate vote exception
        # we try and stop too many votes from the same ip_addr within
        # some time frame
        response = {'status': 'Failed'}

    return HttpResponse(dumps(response),
                        content_type='application/json')

