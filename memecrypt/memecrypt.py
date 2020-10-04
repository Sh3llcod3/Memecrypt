#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   Please note: this program isn't meant to be taken or used seriously,
#   despite of how functional it may or may not be.

try:
    import string
    import sys
    import traceback
    import time
    import easyparse
    import os
    from stat import S_ISFIFO

    from .terminal_colors import colors
    from .utilities import utils

except(ImportError) as import_fail:
    print(f"Memecrypt: {import_fail}")
    print("Please install this module.")
    raise SystemExit(1)

except(SystemError):
    from terminal_colors import colors
    from utilities import utils


class meme_cipher(object):

    def __init__(self, message=None, enc_key=None,
                 show_colors=True):
        self.message = message
        self.enc_key = enc_key
        self.quiet_output = False
        self.key_map = {}
        self.char_set = f"{string.ascii_letters}{string.digits}{string.punctuation}"

        if show_colors:
            self.__add_colors()
        else:
            self.__add_blank_colors()

    def set_quiet(self):
        self.quiet_output = True

    def set_key(self, key_value):
        if key_value in [str(), None]:
            self.__show_error("Key value cannot be empty.")
            return None
        self.enc_key = str(key_value)

    def set_message(self, message_value):
        if message_value in [str(), None]:
            self.__show_error("Plaintext/Ciphertext cannot be empty.")
            return None
        self.message = str(message_value)

    # Encrypt the plaintext.
    def encrypt(self):

        if self.__check_errors():
            return None

        try:
            # Encrypt message
            self.__derive_key_mapping()
            final_ciphertext = str()
            plain_text = utils.enc_b64(self.message)
            for m in plain_text:
                final_ciphertext += self.key_map[m]
            final_ciphertext = utils.enc_b64(final_ciphertext)
            del plain_text
            return final_ciphertext
        except(Exception):
            self.__show_error("Invalid characters found. "
                              "Please check key or message.")
            return None

    # Decrypt the ciphertext.
    def decrypt(self):

        if self.__check_errors():
            return None

        # Decrypt message
        try:
            self.__derive_key_mapping()
            decrypted_text = str()
            ciphertext = utils.dec_b64(self.message)
            for c in ciphertext:
                for i in self.key_map.items():
                    if c == i[1]:
                        decrypted_text += i[0]
            decrypted_text = utils.dec_b64(decrypted_text)
            return decrypted_text
        except(Exception):
            self.__show_error("Invalid characters found. Please check key or message.")
            return None

    def fetch_url(self, content_url):
        import requests

        if not content_url.startswith(("http://", "https://")):
            content_url = "http://" + content_url
        response = requests.get(content_url)

        if response.ok:
            if not self.quiet_output:
                self.green.print_success("Fetched data from URL.")
            return response.text

        else:
            self.__show_error(f"Unable to fetch data from: {content_url}")
            self.__show_error(f"Recieved response Code: {response.status_code} Reason: {response.reason}")
            return None

    def read_file(self, file_path):
        try:
            with open(file_path, "rb") as local_file:
                file_content = local_file.read()
            return utils.dec_utf(file_content)
        except(UnicodeDecodeError):
            self.__show_error(
                "Error: binary data isn't supported yet."
            )
            self.quit_program(1)
        except(FileNotFoundError):
            self.__show_error(f"File: {file_path} not found.")
            return None

    def write_to(self, file_path, contents):
        with open(file_path, "ab+") as open_file:
            open_file.write(utils.enc_utf(contents))

    def __derive_key_mapping(self):
        mapping_tracker = []
        utils.rand_seed(self.enc_key)
        for i in self.char_set:
            rand_value = utils.rand_choc(self.char_set)
            if rand_value in mapping_tracker:
                utils.rand_seed(
                    str().join(
                        [utils.rand_choc(self.char_set) for i in range(len(self.enc_key) * 2)]
                    )
                )
                new_rand_value = utils.rand_choc(self.char_set)
                while new_rand_value in mapping_tracker:
                    new_rand_value = utils.rand_choc(self.char_set)
                self.key_map.update({i: new_rand_value})
                mapping_tracker.append(new_rand_value)
            else:
                self.key_map.update({i: rand_value})
                mapping_tracker.append(rand_value)

    def __check_errors(self):
        if self.message in [None, str()]:
            self.__show_error("Missing plaintext/ciphertext.")
            return True
        elif self.enc_key in [None, str()]:
            self.__show_error("Missing encryption/decyption key.")
            return True

    def __show_error(self, error_str):
        self.yellow.print_status("!", f"Memecrypt: {error_str}")

    @staticmethod
    def quit_program(exit_code=0):
        sys.exit(exit_code)

    # Add the available colors
    def __add_colors(self):
        self.pink = colors('\033[95m')
        self.blue = colors('\033[94m')
        self.green = colors('\033[92m')
        self.yellow = colors('\033[93m')
        self.red = colors('\033[91m')
        self.blank = colors('\033[0m')
        self.deep_blue = colors('\033[1;34;48m')
        self.deep_yellow = colors('\033[1;33;48m')
        self.deep_red = colors('\033[1;31;48m')
        self.deep_green = colors('\033[1;32;48m')
        self.bold = colors('\033[1;39;48m')
        self.marine_blue = colors('\033[0;36;48m')
        self.deep_pink = colors('\033[1;35;48m')
        self.light_blue = colors('\033[1;36;48m')
        self.highlight = colors('\033[1;37;40m')
        self.underline = colors('\u001b[4m')
        self.end_underline = colors('\u001b[0m')
        self.deep_highlight = colors('\u001b[7m')

    # Add blank colors if selected.
    def __add_blank_colors(self):
        self.pink = colors(str())
        self.blue = colors(str())
        self.green = colors(str())
        self.yellow = colors(str())
        self.red = colors(str())
        self.blank = colors(str())
        self.deep_blue = colors(str())
        self.deep_yellow = colors(str())
        self.deep_red = colors(str())
        self.deep_green = colors(str())
        self.bold = colors(str())
        self.marine_blue = colors(str())
        self.deep_pink = colors(str())
        self.light_blue = colors(str())
        self.highlight = colors(str())
        self.underline = colors(str())
        self.end_underline = colors(str())
        self.deep_highlight = colors(str())


def main():

    parser = easyparse.opt_parser()
    parser.add_example("memecrypt -se -i foo -k bar", str())
    parser.add_example("memecrypt --subs -x -f file.txt -k \"a_key\" ", str())
    parser.add_example("memecrypt -sx -i 'lorem ipsum' -k 'some key'", str())
    parser.add_example("memecrypt --subs -e -u cat.thatlinuxbox.com -k 'ascii cat'", str())
    parser.add_arg(
        "-h",
        "--help",
        None,
        "Show this help screen and exit.",
        optional=True
    )
    parser.add_arg(
        "-v",
        "--version",
        None,
        "Print version and exit.",
        optional=True
    )
    parser.add_arg(
        "-s",
        "--subs",
        None,
        "Select the substitution cipher."
    )
    parser.add_arg(
        "-e",
        "--encrypt",
        None,
        "Select encryption mode."
    )
    parser.add_arg(
        "-x",
        "--decrypt",
        None,
        "Select decryption mode."
    )
    parser.add_arg(
        "-k",
        "--key",
        "key",
        "Specify key."
    )
    parser.add_arg(
        "-i",
        "--input",
        "input-string",
        "Specify input string."
    )
    parser.add_arg(
        "-u",
        "--url",
        "url",
        "GETs data from the url."
    )
    parser.add_arg(
        "-f",
        "--file",
        "file-path",
        "Specify input file path."
    )
    parser.add_arg(
        "-q",
        "--quiet",
        None,
        "Only show output. Any errors are still displayed.",
        optional=True
    )
    parser.add_arg(
        "-o",
        "--output-file",
        "file",
        "Specify a file to write to.",
        optional=True
    )
    parser.add_arg(
        "-p",
        "--pipe-input",
        None,
        "Take input from stdin.",
        optional=True
    )
    parser.parse_args()

    # Create our instance of the meme_cipher class
    cipher_instance = meme_cipher()

    if parser.is_present("-h") or len(sys.argv) == 1:
        parser.filename = "memecrypt"
        parser.show_help()
        cipher_instance.quit_program(0)

    if parser.is_present("-v"):
        print("Memecrypt 1.5.0 Copyright (c) 2018-2020 Sh3llcod3")
        cipher_instance.quit_program(0)

    if parser.is_present("-q"):
        cipher_instance.set_quiet()

    # Determine the basic options
    input_source = parser.check_multiple("-i", "-u", "-f", "-p", sep=True)
    if input_source[0]:
        cipher_instance.set_message(parser.value_of("-i"))

    if input_source[1]:
        cipher_instance.set_message(
            cipher_instance.fetch_url(
                parser.value_of("-u")
            )
        )

    if input_source[2]:
        cipher_instance.set_message(
            cipher_instance.read_file(
                parser.value_of("-f")
            )
        )

    if input_source[3] and S_ISFIFO(os.fstat(0).st_mode):
        cipher_instance.set_message(
            sys.stdin.read()
        )

    if parser.is_present("-k"):
        cipher_instance.set_key(parser.value_of("-k"))

    init_mode = parser.check_multiple("-s", "-x", "-e", sep=True)
    if init_mode[0] and init_mode[1]:
        if not parser.is_present("-o"):
            if not parser.is_present("-q"):
                cipher_instance.green.print_success("Decrypted result:")
                print("-" * 20)
            print(cipher_instance.decrypt())
            cipher_instance.quit_program()
        else:
            cipher_instance.write_to(
                parser.value_of("-o"),
                cipher_instance.decrypt()
            )
            cipher_instance.quit_program()
    elif init_mode[0] and init_mode[2]:
        if not parser.is_present("-q"):
            cipher_instance.blue.print_status("!", "Note: Use the same key for decryption.")
        if not parser.is_present("-o"):
            if not parser.is_present("-q"):
                cipher_instance.green.print_success("Encrypted result:")
                print("-" * 20)
            print(cipher_instance.encrypt())
            cipher_instance.quit_program()
        else:
            cipher_instance.write_to(
                parser.value_of("-o"),
                cipher_instance.encrypt()
            )
            cipher_instance.quit_program()


if __name__ == "__main__":
    main()
