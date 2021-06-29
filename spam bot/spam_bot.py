#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:07:19 2021

@author: kali
"""

import pyautogui
import time

words = open("word", 'r')
time.sleep(0)


for word in words:
    pyautogui.typewrite(words)
    pyautogui.press('enter')
    time.sleep(0)
    