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

from itertools import chain
from enum import Enum

author = 'Yaoni'

doc = """
Cycling treatments
"""


class Treatment(Enum):
    # The variable names and their values are arbitrary.
    T1 = 'Treatment 1'
    T2 = 'Treatment 2'
    T3 = 'Treatment 3'
    T4 = 'Treatment 4'


class Constants(BaseConstants):
    name_in_url = 'cycling_treatments'
    players_per_group = None
    num_rounds = 8


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            # This code generates a list with 16 (4*4) treatments:
            #
            # [T1, T2, T3, T4, T1, T2, T3, T4...T1, T2, T3, T4]

            # This is suitable for a session of <= 16 participants.
            # If you have more participants, simply change the following
            # 4 to some larger number.
            self.session.vars['treatments'] = list(
                chain(*[Treatment for _ in range(4)])
            )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()

    def set_treatment(self):
        if self.round_number == 1:
            self.treatment = self.session.vars['treatments'].pop(0).name
        else:
            self.treatment = self.in_round(1).treatment
