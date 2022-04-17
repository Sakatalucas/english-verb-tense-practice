import random

verb_tenses = [
    "Simple Present",
    "Simple Past",
    "Simple Future",
    "Present Continuous",
    "Past Continuous",
    "Future Continuous",
    "Present Perfect",
    "Past Perfect",
    "Future Perfect",
    "Present Perfect Continuous",
    "Past Perfect Continuous",
    "Future Perfect Continuous"
]

verb_tense_index = random.randint(0, 11)

print(verb_tenses[verb_tense_index])
