#!/usr/bin/env python3
"""Refresh calendar.json from Google Calendar's private iCal address.
Usage: CAL_ICS_URL=<secret ical url> python3 tools/cal_sync.py
Covers 7 days back to 70 days ahead, recurring events expanded, IST."""
import os, sys, json, urllib.request, datetime as dt
from zoneinfo import ZoneInfo
import icalendar, recurring_ical_events
TZ = ZoneInfo('Asia/Kolkata')
url = os.environ.get('CAL_ICS_URL', '').strip()
if not url:
    sys.exit('CAL_ICS_URL is not set')
raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'study-shelf-sync'}), timeout=60).read()
cal = icalendar.Calendar.from_ical(raw)
today = dt.datetime.now(TZ).date()
start = dt.datetime.combine(today - dt.timedelta(days=today.weekday() + 7), dt.time(0), TZ)
end = dt.datetime.combine(today + dt.timedelta(days=70), dt.time(0), TZ)
out = []
for e in recurring_ical_events.of(cal).between(start, end):
    if str(e.get('STATUS', '')).upper() == 'CANCELLED':
        continue
    s, f = e['DTSTART'].dt, e['DTEND'].dt if 'DTEND' in e else e['DTSTART'].dt
    if not isinstance(s, dt.datetime):  # all-day events are not study blocks
        continue
    s, f = s.astimezone(TZ), f.astimezone(TZ)
    out.append(dict(t=str(e.get('SUMMARY') or '(no title)'), s=s.isoformat(), e=f.isoformat(), d=str(e.get('DESCRIPTION') or '')[:400]))
out.sort(key=lambda x: (x['s'], x['t']))
new = dict(tz='Asia/Kolkata', source='ical', **{'from': start.date().isoformat(), 'to': (end.date() - dt.timedelta(days=1)).isoformat()}, events=out)
old = {}
try:
    old = json.load(open('calendar.json', encoding='utf-8'))
except Exception:
    pass
cmp = lambda d: {k: v for k, v in d.items() if k != 'updated'}
if cmp(old) == cmp(new):
    print('calendar unchanged,', len(out), 'events')
else:
    new['updated'] = dt.datetime.now(TZ).replace(microsecond=0).isoformat()
    json.dump(new, open('calendar.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('calendar.json updated,', len(out), 'events')
