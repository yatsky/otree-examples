from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class Introduction(Page):
    pass


class PersonalityTest(Page):
    form_model = "player"

    def get_form_fields(self):

        res = ["q_{}".format(str(i + 1)) for i in range(28)]
        shuffle(res)
        return res


page_sequence = [
    Introduction,
    PersonalityTest,
]
