from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class NetworkFormation(Page):
    form_model = 'player'
    def get_form_fields(self):
        return [i.name for i in self.player.get_others_in_group()]


    def before_next_page(self):
        self.player.friends = json.dumps([i.name for i in self.player.get_others_in_group() if getattr(self.player, i.name)])


class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.forming_network()


class Results(Page):
    def vars_for_template(self):
        self.group.forming_network()


page_sequence = [
    NetworkFormation,
    BeforeResultsWP,
    Results,
]
