from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ControlPage(Page):
    """
    Use this page class to control the diplay of its subclass.
    """

    def is_displayed(self):
        # for page P_1, we get number 1
        cur_page_num = int(self.__class__.__name__.split('_')[1])

        # say player's page_mask_in_round is "001"
        # then only when cur_page_num == 3 will we get a 1 from 
        # self.player.page_mask_in_round[cur_page_num - 1]
        # Otherwise we only get 0.
        # Adding 1 && (bitwise and) is just me personally want to explicitly
        # return True or False, instead of 1 or 0.
        return 1 && int(self.player.page_mask_in_round[cur_page_num - 1])


class P_1(ControlPage):
    pass


class P_2(ControlPage):
    pass


class P_3(ControlPage):
    pass


page_sequence = [P_1, P_2, P_3]
