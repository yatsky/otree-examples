from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='personality',
        display_name="Personality test (Likert Chart)",
        num_demo_participants=1,
        app_sequence=['personality'],
    ),
    dict(
        name='multiple_choice_multiple_answer',
        display_name="Multiple-choice Multiple-answer",
        num_demo_participants=1,
        app_sequence=['multiple_choice_multiple_answer'],
    ),
    dict(
        name='randomized_pages',
        display_name="Randomized Pages",
        num_demo_participants=1,
        app_sequence=['randomized_pages'],
    ),
    dict(
        name='cycling_treatments',
        display_name="Cycling Treatments",
        num_demo_participants=4,
        app_sequence=['cycling_treatments'],
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'm%j&+onlt0bl8ycks&i9%&^x1kwk^l*(6f*)+&1qpv^+y#&=!v'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
