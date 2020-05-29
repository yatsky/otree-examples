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
from collections import OrderedDict


author = "Yaoni Wang"

doc = """
Demo of Likert chart
"""


class Constants(BaseConstants):
    name_in_url = "personality"
    players_per_group = None
    num_rounds = 1

    with open(name_in_url + "/questions.txt") as f:
        questions = f.readlines()

    choices_map = OrderedDict(
        (
            (0, "Does not describe me well"),
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "Describe me very well"),
        )
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_fields(questions):
    res = []
    for q in questions:
        res.append(
            models.IntegerField(
                choices=[(i, Constants.choices_map[i]) for i in range(5)],
                label=q,
                widget=widgets.RadioSelect,
            )
        )
    return res


class Player(BasePlayer):
    (
        q_1,
        q_2,
        q_3,
        q_4,
        q_5,
        q_6,
        q_7,
        q_8,
        q_9,
        q_10,
        q_11,
        q_12,
        q_13,
        q_14,
        q_15,
        q_16,
        q_17,
        q_18,
        q_19,
        q_20,
        q_21,
        q_22,
        q_23,
        q_24,
        q_25,
        q_26,
        q_27,
        q_28,
    ) = make_fields(Constants.questions)
