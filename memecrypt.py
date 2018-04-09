#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    MemeCrypt - Encryption algorithms intended for comedic purposes.
    Copyright (C) 2018 Yudhajit N.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    Please note: this program isn't meant to be taken or used seriously,
    despite of how functional it may or may not be.
'''
#Import necessary modules
import random, string, sys, traceback, time, base64, requests, binascii, codecs
#Create a class which will store all colour objects.
color_list = []
class col(object):
    def __init__(self,code):
        self.code = code
        self.status_success = '{}[+]{} '.format(self.code,"\033[0m")
        self.status_fail = '{}[-]{} '.format(self.code,"\033[0m")
        self.status_question = '{}[?]{} '.format(self.code,"\033[0m")
        self.status_unsure = '{}[~]{} '.format(self.code,"\033[0m")
        color_list.append(code)
    def print_success(self, mesg_to_print):
        print(self.status_success + mesg_to_print)
    def print_fail(self, mesg_to_print):
        print(self.status_fail + mesg_to_print)
    def print_question(self, mesg_to_print):
        print(self.status_question + mesg_to_print)
    def print_unsure(self, mesg_to_print):
        print(self.status_unsure + mesg_to_print)
    def print_color(self, mesg_to_print):
        print(self.code + mesg_to_print + "\033[0m")
    def print_custom(self,mesg_to_print,symbol):
        print('{}[{}]{} '.format(self.code,symbol,"\033[0m") + mesg_to_print)
    return_color = lambda self, mesg_to_print: "{}{}{}".format(self.code,mesg_to_print,"\033[0m")
#Add all the colours to col class
head = col('\033[95m')#Bright pink
okb = col('\033[94m')#Standard blue
okg = col('\033[92m')#Standard green
warn = col('\033[93m')#Standard yellow
fail = col('\033[91m')#Standard red
endl = col('\033[0m')#Default white
blue_deep = col('\033[1;34;48m')#Bold blue
warn_deep = col('\033[1;33;48m')#Bold yellow
fail_deep = col('\033[1;31;48m')#Bold red
green_deep = col('\033[1;32;48m')#Bold green
endl_deep = col('\033[1;39;48m')#Default bold
yel_deep = col('\033[1;33;48m')#Bold yellow
marine_blue = col('\033[0;36;48m')#Turquoise blue
head_deep = col('\033[1;35;48m')#Bold pink
light_blue = col('\033[1;36;48m')#Bold light blue
highlight = col('\033[1;37;40m')#Text highlight grey
unline = col('\u001b[4m')#Text underline
unline_end = col('\u001b[0m')#Finish underlining
rev_highlight = col('\u001b[7m')#White highlight black text
#Set the version number
meme_version = "1.0"
#Assign some function aliases
p_write = sys.stdout.write #program write to stdout
#Set a logo
logo = (b"""CgogIF9fICBfXyAgICAgICAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgICAgICAgIF8gICAKIHwgIFwvICB8ICAgICAgICAgICAgICAgICAgICAvIF9fX198ICAgICAgICAgICAgICAgIHwgfCAgCiB8IFwgIC8gfCBfX18gXyBfXyBfX18gICBfX198IHwgICAgIF8gX18gXyAgIF8gXyBfXyB8IHxfIAogfCB8XC98IHwvIF8gXCAnXyBgIF8gXCAvIF8gXCB8ICAgIHwgJ19ffCB8IHwgfCAnXyBcfCBfX3wKIHwgfCAgfCB8ICBfXy8gfCB8IHwgfCB8ICBfXy8gfF9fX198IHwgIHwgfF98IHwgfF8pIHwgfF8gCiB8X3wgIHxffFxfX198X3wgfF98IHxffFxfX198XF9fX19ffF98ICAgXF9fLCB8IC5fXy8gXF9ffAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfXy8gfCB8ICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8X19fL3xffCAgICAgICAgCg==""")
welcome_logo = lambda: print("{}{}{}".format(random.choice(color_list),base64.b64decode(logo).decode('utf-8'),endl.code)) # Pretty colors!
#Why is the logo in base64? Because obfuscation is fun!
#Show warranty information
def display_warranty():
    p_write("\n")
    okg.print_success(okb.return_color("Memecrypt-{} Copyright (C) 2018 Sh3llcod3").format(meme_version))
    endl.print_unsure(head.return_color("This program comes with ABSOLUTELY NO WARRANTY; for details visit: https://goo.gl/W1jcr5."))
    endl.print_unsure(head.return_color("This is free software, and you are welcome to redistribute it"))
    endl.print_unsure(head.return_color("under certain conditions; visit: https://goo.gl/FSy6nc for details."))
    endl.print_unsure(head.return_color("Please follow all instructions that appear. Thanks for using this program.\n"))
#Define the 'meme' class, where all decryption and such will take place
class meme(object):
    def __init__(self,message=str(),key=str()):
        self.message = message
        self.url = str()
        #self.key_map = []
        self.key = key
        self.seeded_charset = []
        self.unique_mapping_tracker = []
        self.charset = string.ascii_letters + string.digits + string.punctuation
    #b64d = lambda self, encoded_text: base64.b64decode(encoded_text).decode('utf-8')
    #b64e = lambda self, plain_text: base64.b64encode(plain_text.encode('utf-8')).decode('utf-8')
    to_utf = lambda self, target_str: target_str.encode('utf-8')
    fr_utf = lambda self, target_byte: target_byte.decode('utf-8')
    to_hex = lambda self, input_str: self.fr_utf(binascii.hexlify(self.to_utf(input_str)))
    fr_hex = lambda self, input_int: self.fr_utf(binascii.unhexlify(self.to_utf(input_int)))
    b_e = lambda self, str_to_encode: self.fr_utf(base64.b64encode(self.to_utf(str_to_encode)))
    b_d = lambda self, base_to_decode: self.fr_utf(base64.b64decode(self.to_utf(base_to_decode)))
    def generate_key(self):
        pass #Now, how do I create an asymetric algorithm from scratch?
    #Calculate the letter substitution mapping.
    def derive_key_mapping(self):
        random.seed(self.key)
        for i in self.charset:
            self.chosen_val = random.choice(self.charset)
            if self.chosen_val in self.unique_mapping_tracker:
                random.seed(''.join([random.choice(self.charset) for i in range(len(self.key)*2)]))
                self.re_chosen_val = random.choice(self.charset)
                while self.re_chosen_val in self.unique_mapping_tracker:
                    self.re_chosen_val = random.choice(self.charset)
                self.seeded_charset.append([i,self.re_chosen_val])
                self.unique_mapping_tracker.append(self.re_chosen_val)
            else:
                self.seeded_charset.append([i,self.chosen_val])
                self.unique_mapping_tracker.append(self.chosen_val)
    #Encrypt the message.
    def encrypt(self):
        self.cipher_text = str()
        self.message = self.b_e(self.message)
        for m in self.message:
            for c in self.seeded_charset:
                if m == c[0]:
                    self.cipher_text += c[1]
        self.cipher_text = self.b_e(self.cipher_text)
        if hasattr(terminal_args,'quiet_output'):
            p_write(self.cipher_text)
        else:
            okb.print_custom("Note: Please use the same key for decryption.","!")
            okg.print_success("Encrypted result: " + self.cipher_text)
    #Decrypt the ciphertext.
    #I am aware of the bad variables names. They were done with find & replace.
    def decrypt(self):
        try:
            self.cipher_text = str()
            self.message = self.b_d(self.message)
            for m in self.message:
                for c in self.seeded_charset:
                    if m == c[1]:
                        self.cipher_text += c[0]
            self.cipher_text = self.b_d(self.cipher_text)
            if hasattr(terminal_args,'quiet_output'):
                p_write(self.cipher_text)
            else:
                okg.print_success("Decrypted result: " + self.cipher_text)
        except(binascii.Error):
            fail.print_fail("Invalid characters found, please check key or message.")
    def entropy(self):
        pass #Fun and chaos, yet to ensue.
    def hash_gen(self,n_digits=32,hash_rounds=1):
        start_time = time.time()
        count = 0
        self.hash_digest = str()
        key_space = string.hexdigits #string.ascii_letters + string.digits
        self.seed_value = binascii.hexlify(self.message.encode('utf-8')).decode('utf-8')
        if len(self.seed_value) < 128:
            remainder = 128 - len(self.seed_value)
            random.seed(self.seed_value)
            padding = ''.join([random.choice(key_space) for i in range(1,remainder+1)])
            self.seed_value += padding
        elif len(self.seed_value) > 128:
            self.seed_value = self.seed_value[:128]
        random.seed(self.seed_value)
        while count < hash_rounds:
            self.hash_digest = ''.join([random.choice(key_space) for i in range(n_digits)])
            random.seed(self.hash_digest)
            count += 1
        end_time = round(time.time() - start_time,4)
        if hasattr(terminal_args,'quiet_output'):
            p_write(self.hash_digest)
        else:
            p_write("\n")
            okg.print_success(fail.return_color("Hash: {}".format(okb.return_color(self.hash_digest))))
            okg.print_unsure(fail.return_color("Rounds: {}".format(okg.return_color(hash_rounds))))
            okg.print_unsure(fail.return_color("Length: {}".format(head.return_color(n_digits))))
            okg.print_unsure(fail.return_color("Input: {}".format(warn.return_color(self.message))))
            okb.print_custom(endl.return_color("Hash computed in {} seconds.".format(end_time)),"i")
            p_write("\n")
#Create the class to process command-line arguments
class args(object):
    #I could have used the argparse module, but I wanted to do it my-self, in my own way.
    #I am aware this is isn't the smartest approach, but I wanted to take a shot at it.
    def __init__(self,arguments):
        self.arguments = arguments
        self.len_args = len(arguments)
        self.pa = 0 #Processed arguments
        self.arg_map = [] #store which argument maps to which function in a 2d list
    def quits(self,exit_code):
        sys.exit(exit_code)
    def display_arg(self,short_arg,long_arg,description,optional_val="none_specified",function_id="optional"):
        if self.show_args == False:
            if function_id == "optional":
                self.arg_map.append([short_arg,long_arg])
            else:
                self.arg_map.append([short_arg,long_arg,function_id])
        initial_string = "       {} {}".format(endl_deep.return_color(short_arg),endl_deep.return_color(long_arg))
        if optional_val != "none_specified":
            initial_string += " {}{}{}".format(unline.code,optional_val,unline_end.code)
        if self.show_args == True:
            print(initial_string)
            print("              {}".format(description))
    def display_version(self):
        display_warranty()
        self.pa += 1
        self.quits(0)
    def fetch_data(self,*arg_tuple):
        try:
            arg_array = []
            arg_list = list(arg_tuple)
            for i in arg_list:
                for q in self.arguments:
                    if i == q:
                        if q not in arg_array:
                            _index = self.arguments.index(q) + 1
                            arg_array.append([q,self.arguments[_index]])
                            self.arguments.remove(q)
                            self.arguments.remove(self.arguments[_index-1])
            return arg_array
        except(ValueError,IndexError) as e:
            fail.print_fail("Arguments not supplied correctly.")
            #print(e)#DEBUG
            #traceback.print_exc()#DEBUG
            self.quits(1)
    is_quiet = lambda self: True if '-q' in self.arguments or '--quiet' in self.arguments else False
    def n_digest(self):
        self.pa += 1
        try:
            function_values = self.fetch_data("-r","--rounds","-n","--number","-i","--input")
            for data in function_values:
                if data[0] in ["-r","--rounds"]:
                    h_rounds = int(data[1])
                if data[0] in ["-n","--number"]:
                    n_length = int(data[1])
                if data[0] in ["-i","--input"]:
                    m_input = data[1]
            if self.is_quiet():
                self.quiet_output = True
            if 'h_rounds' not in locals():
                h_rounds = 1
            if 'n_length' not in locals():
                n_length = 32
        except(TypeError,ValueError):
            h_rounds = 1
            n_length = 32
        try:
            instance = meme(m_input)
            instance.hash_gen(n_length,h_rounds)
        except(UnboundLocalError,ValueError) as error:
            fail.print_fail("Arguments not supplied correctly.")
            self.quits(1)
        #print(function_values)#DEBUG
        self.quits(0)
    #This is a really bad solution, as there is a lot of duplicated code and long lines.
    #I will fix this as soon as I get time.
    def sym_sub_cipher(self):
        self.pa += 1
        if self.is_quiet():
            self.quiet_output = True
        #This is really, really bad code. I will fix this as soon as possible.
        try:
            self_option = ["-s","--substitution"]
            for q in self_option:
                if q in self.arguments:
                    self.arguments.remove(q)
            k_mode = [["-e","e"],["--encrypt","e"],["-x","d"],["--decrypt","d"]]
            for i in k_mode:
                if i[0] in self.arguments:
                    self.arguments.remove(i[0])
                    self.set_mode = i[1]
            cipher_options = self.fetch_data("-i","--input","-c","--ciphertext","-k","--key","-u","--url","-f","--file")
            for data in cipher_options:
                if data[0] in ["-i","--input"] and self.set_mode == "e":
                    self.input_stdin = data[1]
                elif data[0] in ["-c","--ciphertext"] and self.set_mode == "d":
                    self.input_stdin = data[1]
                elif data[0] in ["-u","--url"]:
                    self.url = data[1]
                    response = requests.get(self.url)
                    if response.status_code == 200:
                        self.input_stdin = response.text
                        if not hasattr(self,'quiet_output'):
                            okg.print_success("Successfully fetched data from url.")
                            if len(response.text) > 10000:
                                warn.print_custom("Data is quite large, cipher may take a while.","!")
                    else:
                        fail.print_fail("Failed to get URL contents, code: {}".format(response))
                        self.quits(1)
                    #self.input_stdin = data[1]
                elif data[0] in ["-f","--file"]:
                    try:
                        with open(data[1],"r") as local_file:
                            self.input_stdin = local_file.read()
                            file_len = len(self.input_stdin)
                            if not hasattr(self,'quiet_output'):
                                okg.print_success("Successfully read {} characters from file.".format(file_len))
                                if file_len > 10000:
                                    warn.print_custom("File has lots of lines, cipher may take a while.","!")
                    except(FileNotFoundError):
                        fail.print_fail("File not found, quitting.")
                        self.quits(1)
                    #self.input_stdin = data[1]
                if data[0] in ["-k","--key"] and self.set_mode in ["e","d"]:
                    self.enc_dec_key = data[1]
            cipher_instance = meme(self.input_stdin,self.enc_dec_key)
            cipher_instance.derive_key_mapping()
            if self.set_mode == "e":
                cipher_instance.encrypt()
            elif self.set_mode == "d":
                cipher_instance.decrypt()
            self.quits(0)
        except(UnicodeDecodeError):
            fail.print_fail("Invalid characters found, please check key or message.")
            self.quits(1)
        except(UnboundLocalError,TypeError,ValueError,AttributeError):
            fail.print_fail("Arguments not supplied correctly.")
            #print(e)#DEBUG
            #traceback.print_exc()#DEBUG
            self.quits(1)
    def manage_args(self,print_args):
        self.show_args = print_args
        if print_args == True:
            okg.print_success("Usage: {} [options]".format(fail.return_color(self.arguments[0])))
            okb.print_custom("All valid arguments are as follows:\n","i")
        self.display_arg("-h","--help","Show this help screen and exit.",function_id="self.manage_args(True)")
        self.display_arg("-v","--version","Print version information and exit.",function_id="self.display_version()")
        self.display_arg("-s","--substitution","Use the substitution cipher. Takes -i,-k,-u,-f,-c as valid args.",function_id="self.sym_sub_cipher()")
        self.display_arg("-e","--encrypt","Specify encrypt mode for -s. Needs -i if text is entered by hand.")
        self.display_arg("-x","--decrypt","Specify decrypt mode for -s. Requires use of -c for entered text.")
        self.display_arg("-c","--ciphertext","Specify the ciphertext to work with. Use when -x is used.","ciphertext")
        self.display_arg("-k","--key","Specify the key to use. Needed, if -s is used with -e/-x mode","key")
        self.display_arg("-f","--file","Use local file for input. Works on most functions.","file-path")
        self.display_arg("-u","--url","cURL the contents of the URL for input. Please ensure url starts with 'http://'.","url")
        self.display_arg("-i","--input","Specify the string on which to work on.","input-string")
        self.display_arg("-d","--hash","Hash the input specified by -i and print the digest.",function_id="self.n_digest()")
        self.display_arg("-n","--number","Output a digest of length n (for -d).","n")
        self.display_arg("-r","--rounds","Number of times to run input through the function (for -d)","rounds")
        self.display_arg("-q","--quiet","Less verbose output. Ideal for I/O redirection. Works on all functions.")
        if print_args == True:
            #print(self.arg_map)#DEBUG
            p_write("\n")
            okb.print_custom("Additional arguments are ignored.","i")
            okb.print_custom("If multiple functions are called, the first one above will run.","i")
            okb.print_custom("Some arguments are mutually exclusive, like -c, -u or -f for example.","i")
            okb.print_custom("As of version {} the substition cipher doesn't work with images/binary data yet.".format(meme_version),"i")
            okb.print_custom("If no arguments are valid or present, the menu will lanuch.","i")
            self.pa += 1
            self.quits(0)
    def parse_args(self):
        for current_arg in self.arg_map:
            for i in self.arguments:
                if current_arg[0] == i or current_arg[1] == i:
                    try:
                        if len(current_arg) >= 3:
                            self.arguments.remove(i)
                            eval(current_arg[2])#Controversial?
                    except(IndexError) as __:
                        print(__)
        if self.pa == 0:
            endl_deep.print_unsure("Warning: Invalid arguments found, Ignoring.")
#Enumerate any arguments if ran as an executable
terminal_args = args(sys.argv)
terminal_args.manage_args(False)
#Only process arguments if there are any.
if len(sys.argv) > 1:
    terminal_args.parse_args()
#Get input and return a list with those input values
def ask_input(*questions):#FINISH THIS
    answer_list = []
    curr_answer = None
    #p_write("\n")
    for i in questions:
        curr_answer = input("{}Please input the {} >> ".format(okb.status_question,i))
        answer_list.append(curr_answer)
    return answer_list
#Hashing algorithm
def menu_option_hash_algo():#FINISH THIS
    hash_options = ask_input("message","hash length (Leave blank for 32)","number of rounds (Leave blank for 1)")
    menu_instance = meme(hash_options[0])
    if hash_options[1].isdigit() and hash_options[2].isdigit():
        menu_instance.hash_gen(int(hash_options[1]),int(hash_options[2]))
    else:
        warn.print_custom("Using default number of digits/rounds.","!")
        menu_instance.hash_gen()
#Symetric key algorithm
def menu_option_sym_algo():
    try:
        cipher_options = ask_input("plain-text/cipher-text","key","mode [e]ncrypt/[d]ecrypt")
        mode = cipher_options[2]
        cipher_instance = meme(cipher_options[0],cipher_options[1])
        cipher_instance.derive_key_mapping()
        p_write("\n")
        if mode.lower() not in ["e","d"]:
            fail.print_fail("Not a valid mode. Please try again.")
            sys.exit(1)
        elif mode.lower() == "e":
            cipher_instance.encrypt()
        else:
            cipher_instance.decrypt()
    except(UnicodeDecodeError):
        fail.print_fail("Invalid characters found, please check key or message.")
    finally:
        sys.exit(1)
#Asymetric key algorithm
def menu_option_asym_algo():
    pass #Still to be added
#Create the menu to choose the correct options
def welcome_menu():#FINISH THIS
    #Please note, these modes of operation are merely simulated
    #This program is not meant to provide any actual security
    menu_options = \
    {"Symetric Key substitution cipher.":"menu_option_sym_algo()",
     "Hashing Algorithm.":"menu_option_hash_algo()",
     "Quit program":"sys.exit(0)",
     "Show menu":"main()"}
    menu_list_map = []
    menu_key_list = list(menu_options.keys())
    warn.print_unsure("Currently, the menu can only take text-based inputs (This will change).")
    #warn.print_unsure("Currently, the substition cipher doesn't work with images/binary data yet.")
    warn.print_unsure("Use command-line arguments for file,url input and quiet output options.\n")
    okg.print_success("Please choose your mode of operation (enter number):")
    for i in enumerate(sorted(menu_key_list,key=len,reverse=True),start=1):
        endl.print_custom(i[1],i[0])
        menu_list_map.append([i[1],i[0]])
    p_write("\n")
    menu_choice = str()
    menu_option_processed = False
    while menu_choice == str():
        try:
            menu_choice = int(input("{}Which one do you want to use? >>".format(okb.status_unsure)))
            for i in menu_list_map:
                if menu_choice == i[1]:
                    menu_option_processed = True
                    exec(menu_options[i[0]])
            if menu_option_processed == False:
                raise ValueError
        except(ValueError):
            warn.print_unsure("Please enter a number from 1 to {}".format(len(menu_key_list)))
            menu_choice = str()
def main():
    welcome_logo()
    display_warranty()
    welcome_menu()
#Call the 'main' function and start the program
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt,EOFError):
        sys.exit(1)
    except Exception as some_error:
        print("\n"+"*"*60)
        print(traceback.format_exc())
        print(some_error)
        print("*"*60)
        sys.exit(1)
#Keep track of changes/upcoming features
'''
------------------------------------------------------------
  Features to implement:
    -> Invoke using arguments via the command line.
    -> Add FHS compliancy when dealing with output files.
    -> Cleanup code.
    -> Increase robustness, add error checks.
    -> Create a GIT repo, add README, instructions, etc.
    -> Create a GUI for the program.
    -> Increase security of algorithm.
    -> Add different key lengths & strengths.
    -> Add public/asymetric key mode.
    -> Add symetric key substitution cipher. [DONE]
    -> Add stream cipher mode.
    -> Add custom hashing algorithm. [DONE]
    -> Add an interactive mode/menu.
    -> Create a version without colour.
    -> Add counter to count time taken to encrypt/decrypt.
    -> Add option to select whether to encrypt/decrypt.
    -> Make code PEP8 Compliant.
------------------------------------------------------------
'''
#Don't roll your own crypto they said, so I rolled my own crypto. I mean, my friends aren't cryptanalysts, or I hope so.
