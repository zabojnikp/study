﻿#!/usr/bin/env python3
# Copyright (c) 2008-9 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import random


articles = ["můj", "tvůj", "její", "jeho"]
subjects = ["kočka", "pes", "kůň", "muž", "žena", "kluk", "holka"]
verbs = ["zpívá", "běží", "skáče", "říka", "bojuje", "plave", "vidí",
         "slyší", "cítí", "spí", "hopká", "doufá", "pláče",
         "se směje", "kráčí"]
adverbs = ["hlasitě", "tiše", "rychle", "pomalu", "kvalitně", "hrozně",
           "hrubě", "zdvořile"]

for _ in [1, 2, 3, 4, 5]:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1) == 0:
        print(article, subject, verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, adverb, verb)
