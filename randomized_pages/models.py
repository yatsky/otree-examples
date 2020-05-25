from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import json
from random import shuffle

author = 'Yaoni'

doc = """
Randomized pages
"""


class Constants(BaseConstants):
    name_in_url = 'randomized_pages'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        from .pages import initial_page_sequence

        page_names = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = page_names.copy()
            shuffle(pb)
            p.page_sequence = json.dumps(pb)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    page_sequence = models.StringField()
    q1 = models.BooleanField(
        label="This is the first question. Is it on the first page?",
        widget=widgets.RadioSelectHorizontal,
    )
    q2 = models.BooleanField(
        label="This is the second question. Is it on the second page?",
        widget=widgets.RadioSelectHorizontal,
    )
    q3 = models.BooleanField(
        label="This is the third question. Is it on the third page?",
        widget=widgets.RadioSelectHorizontal,
    )
