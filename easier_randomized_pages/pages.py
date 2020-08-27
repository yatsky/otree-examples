from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ControlPage(Page):
    def is_displayed(self):
        cur_page_num = int(self.__class__.__name__.split('_')[1])

        return cur_page_num // cur_page_num & int(
            self.player.page_mask_in_round[cur_page_num - 1]
        )


class P_1(ControlPage):
    pass


class P_2(ControlPage):
    pass


class P_3(ControlPage):
    pass


page_sequence = [P_1, P_2, P_3]
