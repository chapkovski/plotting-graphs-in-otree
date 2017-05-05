from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class Introduction(Page):
    form_model = models.Player
    form_fields = ['network_data']

class Results(Page):
    ...


page_sequence = [
    Introduction,
    Results,
]
