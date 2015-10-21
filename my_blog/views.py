from forms import MessageForm
from my_blog.models import Message
from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator
from django.template import RequestContext
from django.contrib import auth
from django.utils import timezone

import datetime


def add_message(request, page_number=1):
    messages = Message.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    current_page = Paginator(messages, 5)
    form = MessageForm(request.POST or None)
    if request.user.is_authenticated():
        if form.is_valid():
            message = form.save(commit=False)
            message.mes_user=request.user
            message.date_published=datetime.datetime.now()
            message.save()
            return redirect("/")
    return render_to_response('message.html', {'form': form, 'messages': current_page.page(page_number), 'username': auth.get_user(request).username}, RequestContext(request))








































