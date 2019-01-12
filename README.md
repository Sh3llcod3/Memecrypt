# Memecrypt

Memecrypt is an encryption tool designed for recreational use,
with the purpose of encrypting and sending messages and memes
between your friends. It features a substitution cipher, designed
and made completely from scratch, where text can be encrypted and
decrypted with the same key from a variety of input sources.

Memecrypt can be imported as a python module or used as a standalone
program, depending on which is required.

![GitHub forks](https://img.shields.io/github/forks/Sh3llcod3/Memecrypt.svg?style=for-the-badge&label=Fork)
![GitHub stars](https://img.shields.io/github/stars/Sh3llcod3/Memecrypt.svg?style=for-the-badge&label=Stars)
![GitHub watchers](https://img.shields.io/github/watchers/Sh3llcod3/Memecrypt.svg?style=for-the-badge&label=Watch)

# Prerequisites

- A GNU/Linux based OS (Tested on: Ubuntu 18.04/Kali 2019.1)
- Bash
- Git
- Python3 (pip3, requests)

# Usage

There are 2 main ways to use memecrypt. Both the program
and module usage is covered here.

## Program usage

To use this as a program, start by cloning the repository from GitHub.
Then build the PyPi format package and install it.

```shell
$ git clone https://github.com/Sh3llcod3/Memecrypt.git
$ cd Memecrypt
$ python3 -m pip install --user --upgrade setuptools wheel
$ python3 setup.py sdist bdist_wheel
$ cd dist/ && python3 -m pip install *.whl --user && cd .. && rm build/ dist/ memecrypt.egg-info/ -rf
```

Alternatively, you may install it direct from PyPi, ready for use.

```shell
$ python3 -m pip install memecrypt
```

#### Options

Let's start by viewing all the supported arguments.

```shell
$ memecrypt --help
[+] Usage: memecrypt [options]

[i] Examples:

      memecrypt -se -i foo -k bar

      memecrypt --subs -x -f file.txt -k "super secret"

      memecrypt -sx -c Ciphertext -k key

      memecrypt --subs -e -u cat.thatlinuxbox.com -k lolcat

[i] Positional arguments:

       -s --subs
              Select the substitution cipher.
       -e --encrypt
              Select encryption mode.
       -x --decrypt
              Select decryption mode.
       -k --key key
              Specify the key to use.
       -i --input input-string
              Specify a string to encrypt/decrypt.
       -u --url url
              Fetch the plaintext/ciphertext from the url.
       -f --file file-path
              Use local file for encrypting/decrypting.

[i] Optional arguments:

       -h --help
              Show this help screen and exit.
       -v --version
              Print version information and exit.
       -q --quiet
              Only show output. Any errors are still displayed.
       -o --output-file file
              Specify a file to output to.
```

#### Encryption

Encrypt a message, taking input as an; argument, url
or file, respectively. In each example, different
representations of arguments may have been used or more
options may have been added to display potential permutations.

```shell

# As an argument
$ ./memecrypt.py -se -i "foo bar" -k "lorem ipsum"
[!] Note: Please use the same key for decryption.
[+] Encrypted result:
---------------------
MHFGL1AjdjpSXXx8

# From a URL
$ ./memecrypt.py --subs --encrypt --url cat.thatlinuxbox.com --key "cat"
[+] Fetched data from URL.
[!] Note: Please use the same key for decryption.
[+] Encrypted result:
---------------------
WiJeTFoiXkxaOl5ETDpeREw6XkRMOl5ET.....(and so on).....

# From a local file
$ ./memecrypt.py -se -f <file-path> -k "foobar" -q
NWl8eSlMd35ZXTQxU289Y0ZdNGdGTCdrU2FBQ3pM...(and so on)...

```

#### Decryption

Decrypt a message, again using argument, and local file
respectively. An URL can also be used here, but I didn't
have the time to host a memecrypt encrypted text page.

```shell

# Decrypt as an argument.
./memecrypt.py -sx -i bVQ0cjJfVkY1TGNCKFRWWzIkZVF... -k wow
[+] Decrypted result:
---------------------
Much encryption, very wow

# Decrypt from file
$ ./memecrypt.py --subs --decrypt -f ../../projects/outputfile -k lol
[+] Decrypted result:
---------------------
Cupcake ipsum dolor. Sit amet topping chocolate bar

```

#### Notes

**Arguments can be used in any order, any form and
arguments can be combined, as long as they don't need
a passed value.** A bit like how you would use `ls -al`.

There are more options and ways you can use them.
Please see the help screen for info on the options.

This is just my implementation of memecrypt and you are welcome
to create your own, or improve upon the algorithm.

To create this, I used [Easyparse](https://github.com/Sh3llcod3/Easyparse),
which is a user-friendly, lightweight argument parser that I wrote.


## Module usage

To use Memecrypt as a python3 module, we'll need to install this
from PyPi using [pip3](https://pip.pypa.io/en/stable/).
Simply run `python3 -m pip install memecrypt` to install the
module.

#### Initialising

Let's start by creating an instance of the `meme_cipher` class.

```Python
# Import our module
import memecrypt

# Create an instance
cipher = memecrypt.meme_cipher(message=None, enc_key=None, show_colors=True)

# message is the message to work on
# enc_key is the key
# show_colors=False to turn off all colors

# message, enc_key, show_colors are optional.
# You could simply just do:
cipher = memecrypt.meme_cipher()

```

#### Setting a message

Once you have created an instance of the `meme_cipher` class,
you can set the message at any time, by calling
the method shown below. The message cannot be blank or `None`.
You don't have to use this method for setting the message,
you can simply set the `<object>.message` attribute too.
The method is there for simplicity reasons.

```Python
# Using our previous instance
cipher.set_message("foo")

# We can access/modify this by accessing the message attribute
print(cipher.message)
# Prints: foo

# Let's try and set a blank message.
cipher.set_message(None)
# Prints: [!] Memecrypt: Plaintext/Ciphertext cannot be empty.

```

#### Setting a key

This works the same way as setting a message. As usual, we'll use
our `cipher` instance. Again, the key cannot be blank or `None`.
Similar to before, you can set the key by modifying the `enc_key` attribute.

```Python
# Setting a key
cipher.set_key("bar")

# We can access/modify the key from the enc_key attribute
print(cipher.enc_key)
# Prints: bar

# Same as before, we can't set a blank key
cipher.set_key('')
# Prints: [!] Memecrypt: Key value cannot be empty.

```

#### Encrypting

Once we have set a key and a message, we can encrypt them.
This will return the result. If the key or message is missing,
it will display an error.

```Python
# message => foo, key => bar
cipher.encrypt()
# Returns: 'NEgydQ=='

```

#### Decrypting

Decrypting is a similar process to encrypting. A valid non-empty
key and message is needed, and errors are displayed if any are not
present.

```Python
# message => NEgydQ==, key=> bar
cipher.decrypt()
# Returns: 'foo'

```

#### Input sources

If we wanted, we could also get our message/key text from a local file
or an URL. You don't have to use this of course, you could implement your
own file handing using `with` blocks or get the contents from a url using
requests, urllib3, aiohttp or any module you want. It's simply there for
convenience purposes, but chances are you can do it better.

```Python
# transfer the contents of the url.
cat = cipher.fetch_url("cat.thatlinuxbox.com")
# Returns a ascii cat.
cipher.set_message(cat)
# We just set our message as the ascii cat!

# Read a local file.
foo_file = cipher.read_file("/path/to/file/file.txt")
# foo_file will have contents of file.txt

# Set our message to contents of file.txt
cipher.set_message(foo_file)

```

#### Output files

If you want to write the output to a file, you can simply do:

```Python
# Append to a file. Create file if file non-existent.
cipher.write_to("path/to/file/file.txt", "lorem ipsum dolor")

# Let's put our encrypted output to a file.
cipher.write_to("foo_bar.txt", cipher.encrypt())
```

Like the input sources, you could write your own method of writing to
a file.

# Conclusion

I would like to thank you for taking the time to read this.
I hope it has been useful in explaining Memecrypt and how it
can be used as a module or program. If you have any questions,
please create an issue in GitHub, and I will try my best to respond
to it, as long as its related to memecrypt and its use.

Memecrypt is just one of my 'weekend projects'.
You can view my other projects at my GitHub page,
where I have built a Wireless network auditing
script called [Airscript-ng](https://github.com/Sh3llcod3/Airscript-ng) with quite a few built-in tools,
and [Easyparse](https://github.com/sh3llcod3/Easyparse) a lightweight, user-friendly argument parser.

[GitHub Link](https://github.com/Sh3llcod3/Memecrypt)

# To-do

- [ ] Add support for binary files
- [ ] Add other modes of operation (in progress)
