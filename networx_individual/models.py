from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
an example of dynamic graphing of network data in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'networx_individual'
    players_per_group = None
    num_rounds = 1
    names = ['Roseanne',
             'Trudie',
             'Melodee',
             'Sophie',
             'Nam',
             'Keturah',
             'Etha',
             'Ike',
             'Piedad',
             'Nancy',
             ]

class Subsession(BaseSubsession):
    ...

class Group(BaseGroup):
    pass



class Player(BasePlayer):
    network_data = models.LongStringField()
