import datetime
from pytz import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit


def get_duration(visit):
    visit_end_time = localtime(visit.leaved_at, timezone('UTC'))
    return datetime.timedelta(
        days=visit_end_time.day-visit.entered_at.day,
        hours=visit_end_time.hour-visit.entered_at.hour,
        minutes=visit_end_time.minute-visit.entered_at.minute
    )


def if_visit_long(visit, minutes=60):
    return get_duration(visit) >= datetime.timedelta(minutes=minutes)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard.id)
    this_passcard_visits = []
    for visit in passcard_visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': if_visit_long(visit)
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
