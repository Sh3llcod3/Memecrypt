#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import base64
    import binascii
    import codecs
    import random

except ImportError as import_fail:
    print(f"Import error: {import_fail}")
    print("Please install this module.")
    raise SystemExit(1)


class utils(object):

    def enc_utf(input_str):
        return input_str.encode("utf-8")

    def dec_utf(input_str):
        return input_str.decode("utf-8")

    def enc_hex(input_str):
        return utils.dec_utf(
            binascii.hexlify(
                utils.enc_utf(input_str)
            )
        )

    def dec_hex(input_str):
        return utils.dec_utf(
            binascii.hexlify(
                utils.enc_utf(input_str)
            )
        )

    def enc_b64(input_str):
        return utils.dec_utf(
            base64.b64encode(
                utils.enc_utf(input_str)
            )
        )

    def dec_b64(input_str):
        return utils.dec_utf(
            base64.b64decode(
                utils.enc_utf(input_str)
            )
        )

    def xor_str(input_val1, input_val2):
        xored_str = str()
        for i in zip(input_val1, input_val2):
            xored_str += chr(ord(i[0]) ^ ord(i[1]))
        return xored_str

    def rot13(input_str):
        return codecs.encode(input_str, "rot13")

    def rand_seed(seed_value):
        random.seed(seed_value)

    def rand_choc(input_values):
        return random.choice(input_values)
