from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Event
from .forms import EventForm


def event_list(request):
    events = Event.objects.all()
    paginator = Paginator(events, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    events_paginated = page_obj.object_list
    context = {
        'events': events_paginated,
        'page_obj': page_obj,
        'paginator': paginator,
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
