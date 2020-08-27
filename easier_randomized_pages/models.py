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
    # set this to the number of pages that are to be randomized
    num_rounds = 3

    # This does not need to be a list,
    # Creating this list should be fairly easy
    page_masks = [
        "001",
        "010",
        "100",
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            # player.page_mask should be the same across all rounds
            # every player will randomly get a page_mask
            if self.round_number == 1:
                page_masks = Constants.page_masks.copy()
                shuffle(page_masks)
                p.page_mask = "".join(page_masks)
            else:
                p.page_mask = p.in_round(1).page_order

            # at the start of each round
            # we get the page mask for the round
            # e.g. in round 2, we get the 010 part in 100010001
            p.page_mask_in_round = p.page_order[
                Constants.num_rounds
                * (self.round_number - 1) : Constants.num_rounds
                * self.round_number
            ]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # the page mask for all rounds
    # for a 3-round (3-page) app
    # this would be something like "001100010"
    # this will be the same across all rounds
    page_mask = models.StringField()

    # the page mask for a single round
    # for a 3-round (3-page) app
    # this would be something like "001"
    # this will be different across all rounds
    page_mask_in_round = models.StringField()
