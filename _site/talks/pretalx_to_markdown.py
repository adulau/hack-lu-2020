#!/usr/bin/env python3
# -*- coding: utf-8

from urllib.parse import quote_plus

from pypretalx import PyPretalx
from keys import username, password


url = 'https://cfp.hack.lu'

p = PyPretalx(url=url, username=username, password=password)

talks = p.talks('hacklu19', limit=100)

all_keynotes = '''# Keynotes
'''
all_talks = '''
# Talks
'''
all_workshops = '''
# Workshops
'''

talk_template = '''
## <a name="{escaped_title}"></a>{title}
by {speaker}

{abstract}

{description}

'''

speaker_template = '''
### Bio: <a name="{escaped_speaker}"></a>{speaker}

{bio}

'''

got_recurrent = False

for talk in talks['results']:
    if talk['state'] != 'confirmed':
        print('NOT CONFIRMED', talk['title'])
        continue
    print(talk['title'])
    if talk['title'] == 'Open the safe and get cured.':
        if got_recurrent:
            continue
        else:
            got_recurrent = True
    md_talk = talk_template.format(escaped_title=quote_plus(talk['title']),
                                   title=talk['title'],
                                   speaker=', '.join([speaker['name'] for speaker in talk['speakers']]),
                                   abstract=talk['abstract'].replace('\r', ''),
                                   description=talk['description'].replace('\r', ''))
    for s in talk['speakers']:
        speaker = p.speakers('hacklu19', s['code'])
        bio = speaker['biography']
        if bio:
            bio = bio.replace('\r', '')
        else:
            bio = ''
        md_talk += speaker_template.format(speaker=speaker['name'],
                                           escaped_speaker=quote_plus(speaker['name']),
                                           bio=bio)

    if talk['submission_type']['en'] in ['Short Talk', 'Talk']:
        all_talks += md_talk
    elif talk['submission_type']['en'] in ['Long Workshop', 'Workshop']:
        all_workshops += md_talk
    elif talk['submission_type']['en'] in ['Keynote']:
        all_keynotes += md_talk

headers = '''---
layout: splash
title:  Talks
excerpt: "Talks - Hack.lu 2019"
---

'''

with open('index.md', 'w') as f:
    f.write(headers)
    f.write(all_keynotes)
    f.write(all_talks)
    f.write(all_workshops)
