from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from pytz import timezone


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    localtime_now = datetime.datetime.now(timezone('UTC'))
    '''print(localtime_now)
    print(active_visits[0].entered_at)'''
    non_closed_visits = []
    for active_visit in active_visits:
        entered_at = active_visit.entered_at
        non_closed_visits.append({
            'who_entered': active_visit.passcard.owner_name,
            'entered_at': entered_at,
            'duration': datetime.timedelta(
                days=localtime_now.day-entered_at.day,
                hours=localtime_now.hour-entered_at.hour,
                minutes=localtime_now.minute-entered_at.minute
            )
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
