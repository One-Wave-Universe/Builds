#!/usr/bin/env python3
SLOTS = [
    {"gray": "C", "polarity": "express", "tag": "P1-E", "midi": 60},
    {"gray": "G", "polarity": "compress", "tag": "P2-C", "midi": 67},
    {"gray": "D", "polarity": "express", "tag": "P3-E", "midi": 62},
    {"gray": "A", "polarity": "compress", "tag": "P4-C", "midi": 69},
    {"gray": "E", "polarity": "express", "tag": "P5-E", "midi": 64},
    {"gray": "B", "polarity": "compress", "tag": "P6-C", "midi": 71},
    {"gray": "F#", "polarity": "compress", "tag": "P1-C", "midi": 66},
    {"gray": "C#", "polarity": "express", "tag": "P2-E", "midi": 61},
    {"gray": "G#", "polarity": "compress", "tag": "P3-C", "midi": 68},
    {"gray": "D#", "polarity": "express", "tag": "P4-E", "midi": 63},
    {"gray": "A#", "polarity": "compress", "tag": "P5-C", "midi": 70},
    {"gray": "F", "polarity": "express", "tag": "P6-E", "midi": 65},
]

def slot_at(t: int) -> dict:
    return SLOTS[t % len(SLOTS)]
