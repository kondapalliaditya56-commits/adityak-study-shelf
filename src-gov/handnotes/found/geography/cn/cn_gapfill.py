# -*- coding: utf-8 -*-
"""Gap fill found by the cross-format sync audit (Shelf/textbook facts missing from the handwritten notes). Source: the Shelf chapter text (handout)."""
from dsl import *
from hwlib import P
ADD = {
 1: [
  dict(after='EARTH FACTS, MAGNETISM', nodes=[
    bx('bl', '<b>Magnetic field shifts:</b> the field keeps moving and <b>reverses about every 2,00,000 to 3,00,000 years</b>; caused by material inside the Earth, so reversal shows that this material can move (an indirect source on the interior).')]),
  dict(after='ECLIPSES, LATITUDE, TIME', nodes=[
    tb(['PYQ: more than four time zones?', 'Time zones (handout answer: only four of the five)'],
       ['<b>United Kingdom</b>', 'mainland GMT/BST (1 zone); with overseas territories (Bermuda, Falklands, Gibraltar) <b>up to 9</b>'],
       ['<b>Denmark</b>', 'mainland UTC+1; Greenland: Danmarkshavn UTC+0, Ittoqqortoormiit UTC−1, Nuuk UTC−3, Thule UTC−4: <b>5</b>'],
       ['<b>New Zealand</b>', 'mainland UTC+12/+13; Tokelau UTC+13, Cook Islands UTC−10, Niue UTC−11: <b>5</b>'],
       ['<b>Australia</b>', 'mainland AWST UTC+8, ACST UTC+9:30, AEST UTC+10; Lord Howe UTC+10:30, Norfolk UTC+11, Cocos UTC+6:30, Christmas UTC+7: <b>6+</b>'],
       ['<b>Brazil</b>', 'historically 4 zones (UTC−2 to UTC−5), now 3 official: <b>not more than 4</b>'])]),
 ],
 2: [
  dict(after='ATMOSPHERE: LAYERS AND GASES', nodes=[
    bx('bl', '<b>CO<sub>2</sub>:</b> about <b>0.038% (now 0.04%)</b> of dry air; product of combustion; greenhouse gas that helps keep the heat budget. <b>Ionosphere:</b> ionised by solar and cosmic radiation; lies <b>75-1000 km</b> above the Earth (thin against the Earth\'s radius of 6370 km).')]),
  dict(after='PRESSURE, PRESSURE BELTS', nodes=[
    bx('bl', 'Pressure belts in both hemispheres stay <b>balanced</b> when the Sun is vertical over the Equator: <b>21 March and 23 September</b> (equinoxes).')]),
 ],
 3: [
  dict(after='TEMPERATURE, SALINITY, DENSITY', nodes=[
    bx('bl', '<b>Deep ocean (abyssal zone, below the thermocline):</b> uniform and cold, about <b>2°C to 4°C</b>; unaffected by solar heating (volcanic hot spots are the exception).')]),
  dict(after='TIDES AND WAVES', nodes=[
    bx('bl', '<b>Tsunami, human cause:</b> nuclear explosions, e.g. US nuclear testing at the <b>Marshall Islands</b> (1940s and 1950s).')]),
  dict(after='CRYOSPHERE', nodes=[
    bx('bl', '<b>Climate change and cities:</b> a <b>quarter of the world\'s urban population</b> faces a <b>0.5°C</b> rise by <b>2040</b>: health risks, lower labour productivity, more cooling demand, more extreme weather.')]),
 ],
 6: [
  dict(after='ENERGY: RENEWABLES, NUCLEAR', nodes=[
    bx('bl', '<b>Why not cover deserts with panels?</b> Just <b>1.2% of the Sahara</b> could power the world, but dark panels absorb more heat, raise temperature and change rain and wind nearby; plus high logistics and maintenance costs (sand cover).')]),
  dict(after='ROADS AND RAILWAYS', nodes=[
    t('<b>NH numbering</b> (new system 2010; earlier under NH Act 1956)',
      '<b>North-South = even numbers</b>, rising from <b>east to west</b> (NH2 east, NH68 west)',
      '<b>East-West = odd numbers</b>, rising from <b>north to south</b> (NH1 north, NH87 south)',
      'Branch (sub-highway): prefix on the parent number, e.g. <b>NH101</b> from NH01',
      '<b>1 April 2018:</b> lane system, each lane\'s length counted separately', w=26),
    bx('ye', '<b>PYQ 2014 (answer D, none matched):</b> <b>NH 4</b> = Andaman Trunk Road, <b>230.7 km</b> (old NH 4 Mumbai-Pune-Hubli-Bangalore-Chennai is now <b>NH 48</b>); <b>NH 6</b> = Jorabat (Meghalaya) to Selling (Mizoram); <b>NH 15</b> = Baihata (Assam) to Wakro (Arunachal).')]),
 ],
}
