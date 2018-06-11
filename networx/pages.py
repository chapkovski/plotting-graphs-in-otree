from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class NetworkFormation(Page):
    form_model =   'player'
    form_fields = ['friends']


class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.forming_network()


class Results(Page):
    ...


page_sequence = [
    NetworkFormation,
    BeforeResultsWP,
    # Results,
]
