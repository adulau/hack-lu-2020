#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib.parse import quote_plus
from datetime import datetime

with open('export.json') as f:
    export = json.load(f)

header_talks = '''
# Talk Agenda

'''

header_Workshops = '''
# Workshops Agenda

'''


day_header_talks = '''

## {date} (Talk)

{{: class="table table-striped"}}

| Time | Talks and Speakers |
|:----:|:------------------:|
'''

talk_days = []

for day in export['schedule']['conference']['days']:
    d = datetime.strptime(day['date'], '%Y-%m-%d')
    md_day = day_header_talks.format(date=d.strftime('%A %d %B %Y'))
    for talk in day['rooms']['Europe']:
        md_day += '| {time} | [{title}](http://2018.hack.lu/talks/#{link}) '.format(time=talk['start'], title=talk['title'], link=quote_plus(talk['title']))
        md_day += '('
        md_day += ', '.join(['[{speaker}](http://2018.hack.lu/talks/#{link})'.format(speaker=speaker['name'], link=quote_plus(speaker['name'])) for speaker in talk['persons']])
        md_day += ') |\n'
    md_day += '{: class="table"}'
    talk_days.append(md_day)

day_header_workshops = '''

## {date} (Workshops)

{{: class="table table-striped"}}

| Time | Hollenfels | Vianden - Wiltz |Echternach - Diekirch | Schengen |
|:----:|:----------:|:---------------:|:--------------------:|:--------:|
'''

workshop_days = []

for day in export['schedule']['conference']['days']:
    d = datetime.strptime(day['date'], '%Y-%m-%d')
    md_day = day_header_workshops.format(date=d.strftime('%A %d %B %Y'))
    # We have only two workshops/room/day so let's make it quick and dirty.
    md_day += '| 09:30 |'
    for room in ["Hollenfels", "Vianden - Wiltz", "Echternach - Diekirch", "Schengen"]:
        if day['rooms'][room] and day['rooms'][room][0]['start'] == '09:30':
            talk = day['rooms'][room][0]
            md_day += '[{title}](http://2018.hack.lu/talks/#{link}) '.format(time=talk['start'], title=talk['title'], link=quote_plus(talk['title']))
            md_day += '('
            md_day += ', '.join(['[{speaker}](http://2018.hack.lu/talks/#{link})'.format(speaker=speaker['name'], link=quote_plus(speaker['name'])) for speaker in talk['persons']])
            md_day += ') |'
        else:
            if day['rooms'][room] and day['rooms'][room][0]['start'] != '13:30':
                print(day['rooms'][room])
            md_day += '|'

    md_day += '\n| 13:30 |'
    for room in ["Hollenfels", "Vianden - Wiltz", "Echternach - Diekirch", "Schengen"]:
        if day['rooms'][room]:
            if day['rooms'][room][0]['start'] == '13:30':
                talk = day['rooms'][room][0]
                md_day += '[{title}](http://2018.hack.lu/talks/#{link}) '.format(time=talk['start'], title=talk['title'], link=quote_plus(talk['title']))
                md_day += '('
                md_day += ', '.join(['[{speaker}](http://2018.hack.lu/talks/#{link})'.format(speaker=speaker['name'], link=quote_plus(speaker['name'])) for speaker in talk['persons']])
                md_day += ') |'
            elif day['rooms'][room][1]['start'] == '13:30':
                talk = day['rooms'][room][1]
                md_day += '[{title}](http://2018.hack.lu/talks/#{link}) '.format(time=talk['start'], title=talk['title'], link=quote_plus(talk['title']))
                md_day += '('
                md_day += ', '.join(['[{speaker}](http://2018.hack.lu/talks/#{link})'.format(speaker=speaker['name'], link=quote_plus(speaker['name'])) for speaker in talk['persons']])
                md_day += ') |'
        else:
            if day['rooms'][room] and day['rooms'][room][0]['start'] != '09:30':
                print(day['rooms'][room])
            md_day += '|'

    md_day += '\n'
    md_day += '{: class="table"}'
    workshop_days.append(md_day)


headers = '''---
layout: splash
title:  Agenda
excerpt: "Agenda - Hack.lu 2018"
---
'''

with open('index.md', 'w') as f:
    f.write(headers)
    f.write('\n'.join(talk_days))
    f.write('\n'.join(workshop_days))
