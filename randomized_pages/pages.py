from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json


class SimpleTemplate(Page):
    def vars_for_template(self):
        return {'title': "Question " + str(self.question_no)}


class Q1(SimpleTemplate):
    form_model = 'player'
    form_fields = ['q1']


class Q2(SimpleTemplate):
    form_model = 'player'
    form_fields = ['q2']


class Q3(SimpleTemplate):
    form_model = 'player'
    form_fields = ['q3']


class Results(Page):
    pass


initial_page_sequence = [Q1, Q2, Q3]

last_sequence = [Results]

page_sequence = []


class MyPage(SimpleTemplate):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split("_")[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.question_no = page_seq + 1
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])

page_sequence = page_sequence + last_sequence
