from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import json
from django.db import models as djmodels

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
an example of dynamic graphing of network data in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'networx_custom'
    players_per_group = 3
    with open('networx_custom/names.txt') as f:
        names = f.read().splitlines()
    num_rounds = 1
    players_per_group = len(names)




class Subsession(BaseSubsession):
    def creating_session(self):
        num_players_err = 'Too many participants for such a short name list'
        if self.session.mturk_num_participants > 0:
            num_participants = self.session.mturk_num_participants
        else:
            num_participants = self.session.num_participants
        assert len(Constants.names) <= num_participants, num_players_err
        for g in self.get_groups():
            cur_names = Constants.names.copy()
            random.shuffle(cur_names)
            for i, p in enumerate(g.get_players()):
                p.name = cur_names[i]
                # we create a set of empty links for each player towards each player
                for o in p.get_others_in_group():
                    p.links_from.create(target=o)


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
    def get_friends(self):
        return json.dumps(list(self.links_from.filter(edge=True).values_list('target__name', flat=True)))


class Link(djmodels.Model):
    source = djmodels.ForeignKey(to=Player, related_name='links_from')
    target= djmodels.ForeignKey(to=Player, related_name='links_to')
    edge = models.BooleanField(blank=True, widget=widgets.CheckboxInput)
