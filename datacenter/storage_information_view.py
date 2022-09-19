from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from pytz import timezone
from datacenter.passcard_info_view import get_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    localtime_now = datetime.datetime.now(timezone('UTC'))
    non_closed_visits = []
    for active_visit in active_visits:
        entered_at = active_visit.entered_at
        non_closed_visits.append({
            'who_entered': active_visit.passcard.owner_name,
            'entered_at': entered_at,
            'duration': get_duration(active_visit)
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
