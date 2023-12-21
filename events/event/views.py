from django.shortcuts import render, get_object_or_404, redirect

from .models import Event
from .forms import EventForm


def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'event/list.html', context)


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event': event,
    }
    return render(request, 'event/detail.html', context)


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event:event_list')
    else:
        form = EventForm()
    context = {
        'form': form,
    }
    return render(request, 'event/update.html', context)


def event_update(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event:event_detail', id=id)
    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'event/update.html', context)
