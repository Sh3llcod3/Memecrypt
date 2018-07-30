#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   utilities.py - Helper functions for memecrypt.
#    Copyright (C) 2018 Yudhajit N. (Sh3llcod3)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>
#   Contact: Please create a issue on my GitHub <https://github.com/Sh3llcod3>
#

# Import needed modules
try:
    import base64
    import binascii
    import codecs
    import random
except(ImportError, ModuleNotFoundError) as import_fail:
    print("Memecrypt: {}".format(import_fail))
    print("Please install this module.")
    raise SystemExit(1)

# Create our utility class
class utils(object):
    '''
    This is the utility class. This class
    will contain useful helper functions,
    including but not limited to:

        -> Encoding to and from UTF-8
        -> Encoding to and from Hex
        -> Encoding to and from Base64
        -> XOR'ing blocks of text
        -> ROT13'ing twice! :)

    Yes, I am aware, that there
    is probably a swiss army knife
    module that does all the above,
    but I wish to create my own anyway.
    '''

    # Encode a str with utf-8
    def enc_utf(input_str):
        return input_str.encode("utf-8")

    # Decode the utf-8 str
    def dec_utf(input_str):
        return input_str.decode("utf-8")

    # Encode to hex
    def enc_hex(input_str):
        return utils.dec_utf(
            binascii.hexlify(
                utils.enc_utf(input_str)
            )
        )

    # Decode from hex
    def dec_hex(input_str):
        return utils.dec_utf(
            binascii.hexlify(
                utils.enc_utf(input_str)
            )
        )

    # Encode to base64
    def enc_b64(input_str):
        return utils.dec_utf(
            base64.b64encode(
                utils.enc_utf(input_str)
            )
        )

    # Decode base64 str
    def dec_b64(input_str):
        return utils.dec_utf(
            base64.b64decode(
                utils.enc_utf(input_str)
            )
        )

    # XOR two strings
    def xor_str(input_val1, input_val2):
        xored_str = str()
        for i in zip(input_val1, input_val2):
            xored_str += chr(ord(i[0]) ^ ord(i[1]))
        return xored_str

    # ROT13 a string
    def rot13(input_str):
        return codecs.encode(input_str, "rot13")

    # Seed the PRNG
    def rand_seed(seed_value):
        random.seed(seed_value)

    # Choose a random value
    def rand_choc(input_values):
        return random.choice(input_values)
