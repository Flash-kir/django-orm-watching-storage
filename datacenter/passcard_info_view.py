from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from django.shortcuts import get_object_or_404


def get_duration(visit):
    if visit.leaved_at:
        visit_end_time = visit.leaved_at
    else:
        visit_end_time = localtime(timezone('UTC'))
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
    print(this_passcard_visits)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
