from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .forms import LinkFormset


class NetworkFormation(Page):
    def vars_for_template(self):
        return {'formset': LinkFormset(instance=self.player)}

    def post(self):
        context = super().get_context_data()
        formset = LinkFormset(self.request.POST, instance=self.player)
        context['formset'] = formset
        context['form'] = self.get_form()
        if formset.is_valid():
            formset.save(commit=True)
        else:
            return self.render_to_response(context)
        return super().post()

    def before_next_page(self):
        print(self.player.get_friends())
        self.player.friends = self.player.get_friends()

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
