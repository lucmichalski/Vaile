#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def asm(headers, content):
    detect = False
    detect |= search(r'The requested URL was rejected. Please consult with your administrator.', content, I) is not None
    if detect:
        return "Application Security Manager (F5 Networks)"
