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
from random import shuffle


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'easier_randomized_pages'
    players_per_group = None
    num_rounds = 3

    # this has to be preset
    # but creating this list should be fairly easy
    page_masks = [
        "001",
        "010",
        "100",
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == 1:
                page_masks = Constants.page_masks.copy()
                shuffle(page_masks)
                p.page_mask = "".join(page_masks)
            else:
                p.page_mask = p.in_round(1).page_order

            p.page_mask_in_round = p.page_order[
                Constants.num_rounds
                * (self.round_number - 1) : Constants.num_rounds
                * self.round_number
            ]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    page_mask = models.StringField()
    page_mask_in_round = models.StringField()
