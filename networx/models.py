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
            for i, p in enumerate(g.get_players()):
                p.name = cur_names[i]


class Group(BaseGroup):
    network_data = models.LongStringField()

    def forming_network(self):
        nodes = [{'data': {'id': i, 'name': i}, 'group': 'nodes'} for i in Constants.names]
        edges = []
        for p in self.get_players():
            friends = json.loads(p.friends)
            edges.extend(
                [{'data': {'id': p.name + i, 'source': p.name, 'target': i}, 'group': 'edges'} for i in friends])
        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                             })


class Player(BasePlayer):
    name = models.StringField()
    friends = models.LongStringField()


for i in Constants.names:
    Player.add_to_class(i, models.BooleanField(widget=widgets.CheckboxInput, blank=True))
