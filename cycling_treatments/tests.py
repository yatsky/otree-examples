from otree.api import Currency as c, currency_range, expect
from . import pages
from ._builtin import Bot
from .models import Constants, Treatment


class PlayerBot(Bot):
    def play_round(self):

        yield pages.MyPage

        print(self.participant.id_in_session)
        if self.participant.id_in_session == 1:
            expect(self.player.treatment, "==", Treatment.T1.name)
        if self.participant.id_in_session == 2:
            expect(self.player.treatment, "==", Treatment.T2.name)
        if self.participant.id_in_session == 3:
            expect(self.player.treatment, "==", Treatment.T3.name)
        if self.participant.id_in_session == 4:
            expect(self.player.treatment, "==", Treatment.T4.name)
