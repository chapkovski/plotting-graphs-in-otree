from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import json
from django import forms

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
an example of dynamic graphing of network data in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'networx'
    players_per_group = 3
    num_rounds = 1
    names = ['Roseanne',
             'Trudie',
             'Melodee',
             ]

class Subsession(BaseSubsession):
    def creating_session(self):
        for g in self.get_groups():
            cur_names = Constants.names.copy()
            random.shuffle(cur_names)
            for i,p in enumerate(g.get_players()):
                p.name = cur_names[i]


class Group(BaseGroup):
    network_data = models.LongStringField()
    def forming_network(self):
        ...



class Player(BasePlayer):
    name = models.StringField()
    friends  = models.LongStringField()
