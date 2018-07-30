#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    MemeCrypt - Encryption algorithm intended for comedic purposes.
#    Copyright (C) 2018 Yudhajit N.
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
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    Please note: this program isn't meant to be taken or used seriously,
#    despite of how functional it may or may not be.
#

try:
    # Import standard (usually) built-in modules
    import string
    import sys
    import traceback
    import time
    import requests
    import easyparse

    # Import custom modules
    from .terminal_colors import colors
    from .utilities import utils

except(ImportError) as import_fail:
    print("Memecrypt: {}".format(import_fail))
    print("Please install this module.")
    raise SystemExit(1)
except(SystemError):
    from terminal_colors import colors
    from utilities import utils


# Create our main class.
class meme_cipher(object):
    '''
    This is our cipher class. This is where
    all encryption, decryption and such
    will take place.
    '''

    def __init__(self, message=None, enc_key=None,
                 show_colors=True):
        self.message = message
        self.enc_key = enc_key
        self.quiet_output = False
        self.key_map = {}
        self.char_set = ( string.ascii_letters +
                          string.digits +
                          string.punctuation )

        # Set the colors
        if show_colors:
            self.__add_colors()
        else:
            self.__add_blank_colors()

    # Set the quiet_output attribute.
    def set_quiet(self):
        self.quiet_output = True

    # Add the key to encrypt
    def set_key(self, key_value):
        if key_value in [str(), None]:
            self.__show_error("Key value cannot be empty.")
            return None
        self.enc_key = str(key_value)

    # Add the plaintext/ciphertext
    def set_message(self, message_value):
        if message_value in [str(), None]:
            self.__show_error("Plaintext/Ciphertext cannot be empty.")
            return None
        self.message = str(message_value)

    # Encrypt the plaintext.
    def encrypt(self):

        # Check for errors
        if self.__check_errors():
            return None

        try:
            # Encrypt message
            self.__derive_key_mapping()
            final_ciphertext = str()
            plain_text = utils.enc_b64(self.message)
            #self.message = utils.enc_b64(self.message)
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

        # Check for errors
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
            self.__show_error("Invalid characters found. "
                              "Please check key or message.")
            return None

    # Add method to get contents from url.
    def fetch_url(self, content_url):
        if not content_url.startswith(("http://", "https://")):
            content_url = "http://" + content_url
        response = requests.get(content_url)

        # Check if response is valid.
        if response.ok:
            if not self.quiet_output:
                self.green.print_success("Fetched data from URL.")
            return response.text
        else:
            self.__show_error("Unable to fetch data from: {}".format(
                content_url
            ))
            self.__show_error("Recieved response Code: {} Reason: {}".format(
                response.status_code,
                response.reason
            ))
            return None

    # Add method to read from file
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
            self.__show_error("File: {} not found.".format(file_path))
            return None

    # Write out contents to file.
    def write_to(self, file_path, contents):
        with open(file_path, "ab+") as open_file:
            open_file.write(utils.enc_utf(contents))

    # Calulate the mapping for encrypting/decrypting
    def __derive_key_mapping(self):
        mapping_tracker = []
        utils.rand_seed(self.enc_key)
        for i in self.char_set:
            rand_value = utils.rand_choc(self.char_set)
            if rand_value in mapping_tracker:
                utils.rand_seed(
                    str().join(
                        [utils.rand_choc(self.char_set) for i in range(len(self.enc_key)*2)]
                    )
                )
                new_rand_value = utils.rand_choc(self.char_set)
                while new_rand_value in mapping_tracker:
                    new_rand_value = utils.rand_choc(self.char_set)
                self.key_map.update({i : new_rand_value})
                mapping_tracker.append(new_rand_value)
            else:
                self.key_map.update({i : rand_value})
                mapping_tracker.append(rand_value)

    # Check for missing values
    def __check_errors(self):
        if self.message in [None, str()]:
            self.__show_error("Missing plaintext/ciphertext.")
            return True
        elif self.enc_key in [None, str()]:
            self.__show_error("Missing encryption/decyption key.")
            return True

    # method for displaying errors
    def __show_error(self, error_str):
        self.yellow.print_status("!", "Memecrypt: {}".format(
            error_str
        ))

    # Quit the program
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

# Run as command-line program, if not imported.
def main():

    # Set up the arugment parser with the arguments.
    parser = easyparse.opt_parser()
    parser.add_example("-se -i foo -k bar")
    parser.add_example("--subs -x -f file.txt -k \"super secret\" ")
    parser.add_example("-sx -c Ciphertext -k key")
    parser.add_example("--subs -e -u cat.thatlinuxbox.com -k lolcat")
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
        "Print version information and exit.",
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
        "Specify the key to use."
        )
    parser.add_arg(
        "-i",
        "--input",
        "input-string",
        "Specify a string to encrypt/decrypt."
        )
    parser.add_arg(
        "-u",
        "--url",
        "url",
        "Fetch the plaintext/ciphertext from the url."
        )
    parser.add_arg(
        "-f",
        "--file",
        "file-path",
        "Use local file for encrypting/decrypting."
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
        "Specify a file to output to.",
        optional=True
        )
    parser.parse_args()

    # Create our instance of the meme_cipher class
    cipher_instance = meme_cipher()

    # View the help screen
    if parser.is_present("-h") or len(sys.argv) == 1:
        parser.show_help()
        cipher_instance.quit_program(0)

    # Show version information.
    if parser.is_present("-v"):
        print("Memecrypt Copyright (C) 2018 Yudhajit N.")
        print("License GPLv3+: GNU GPL version 3 "
              "or later <http://gnu.org/licenses/gpl.html>.")
        print("This is free software: "
              "you are free to change and redistribute it.")
        print("There is NO WARRANTY, to the extent permitted by law.\n")
        cipher_instance.quit_program(0)

    # Process the arguments and get data from them.

    if parser.is_present("-q"):
        cipher_instance.set_quiet()

    # Determine the basic options
    input_source = parser.check_multiple("-i","-u","-f", sep=True)
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
    if parser.is_present("-k"):
        cipher_instance.set_key(parser.value_of("-k"))

    init_mode = parser.check_multiple("-s","-x","-e", sep=True)
    if init_mode[0] and init_mode[1]:
        if not parser.is_present("-o"):
            if not parser.is_present("-q"):
                cipher_instance.green.print_success("Decrypted result:")
                print("-"*21)
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
            cipher_instance.blue.print_status("!",
                "Note: Please use the same key for decryption."
            )
        if not parser.is_present("-o"):
            if not parser.is_present("-q"):
                cipher_instance.green.print_success("Encrypted result:")
                print("-"*21)
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

# ----------------------------------------
# > Don't roll your own crypto they said.
# > They were wrong.
# > so I rolled my own crypto.
# > What could possibly go wrong?
# ----------------------------------------
