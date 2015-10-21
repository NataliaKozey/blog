from django.forms import ModelForm
from models import Message, User
from django.contrib.auth import authenticate, get_user_model
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.forms import User
from django.db.models import Q

class MessageForm(ModelForm):

    class Meta:
        model = Message

        exclude = ['mes_user', 'date_published' ]


