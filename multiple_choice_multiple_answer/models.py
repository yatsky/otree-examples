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

from django.forms.widgets import CheckboxSelectMultiple

author = 'Yaoni'

doc = """
Multiple choice, multiple answer fields.
"""


class Constants(BaseConstants):
    name_in_url = 'multiple_choice_multiple_answer'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    love_this = models.StringField(
        label="Easily choose multiple answers!",
        widget=CheckboxSelectMultiple(
            choices=(
                # or use (number, string) pair
                # if you want better data analysis
                # (1, "This is awesome!"),
                ("This is awesome!", "This is awesome!"),
                ("Great!", "Great!"),
                ("I love this!", "I love this!"),
                ("Don't like it (really?💣)", "Don't like it (really?💣)"),
            )
        ),
    )
