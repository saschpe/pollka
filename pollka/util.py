# -*- coding: utf-8 -*-

import base64
import hashlib
import random


def generate_short_hash(length=12):
    '''Returns a short hash that can be used in URLs.
    '''
    if (length > 22):  # Make sure we don't get padding '=' from Base64 encoding
        length = 22
    return base64.urlsafe_b64encode(hashlib.md5(str(random.random())).digest())[:length]
